from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Video, Summary
import os
import json

@api_view(['POST'])
def upload_video(request):
    try:
        youtube_url = request.data.get('youtube_url', '')
        video_file = request.FILES.get('video_file')
        summary_type = request.data.get('summary_type', 'short')

        if not youtube_url and not video_file:
            return Response(
                {'error': 'Please provide video file or YouTube URL'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save video to database
        video = Video.objects.create(
            title=f'Video - {youtube_url[:50] if youtube_url else video_file.name}',
            youtube_url=youtube_url if youtube_url else None,
            status='processing'
        )

        if video_file:
            video.file_path = video_file
            video.save()

        return Response({
            'message': 'Video uploaded successfully!',
            'video_id': video.id,
            'status': 'processing'
        })

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
def summarize_video(request):
    try:
        video_id = request.data.get('video_id')
        
        if not video_id:
            return Response(
                {'error': 'video_id required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        video = Video.objects.get(id=video_id)

        # AI Processing
        transcript = transcribe_video(video)
        summary = generate_summary(transcript)
        key_points = generate_key_points(transcript)

        # Save to database
        Summary.objects.create(
            video=video,
            summary_text=summary,
            key_points=json.dumps(key_points),
            transcript=transcript,
        )

        video.status = 'done'
        video.save()

        return Response({
            'summary': summary,
            'key_points': key_points,
            'transcript': transcript,
            'status': 'success'
        })

    except Video.DoesNotExist:
        return Response(
            {'error': 'Video not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


def transcribe_video(video):
    try:
        import whisper
        model = whisper.load_model("base")

        if video.youtube_url:
            import yt_dlp
            audio_path = f"media/audio_{video.id}.mp3"
            os.makedirs("media", exist_ok=True)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': audio_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video.youtube_url])
            result = model.transcribe(audio_path + ".mp3")
        else:
            result = model.transcribe(video.file_path.path)

        return result["text"]

    except Exception as e:
        return f"Transcription error: {str(e)}"


def generate_summary(transcript):
    try:
        from transformers import pipeline
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )
        max_input = min(len(transcript), 1024)
        result = summarizer(
            transcript[:max_input],
            max_length=150,
            min_length=50,
            do_sample=False
        )
        return result[0]['summary_text']
    except Exception as e:
        return f"Summary error: {str(e)}"


def generate_key_points(transcript):
    sentences = transcript.split('.')
    key_points = []
    for sentence in sentences[:5]:
        sentence = sentence.strip()
        if len(sentence) > 20:
            key_points.append(sentence)
    return key_points if key_points else ["Key point extraction complete"]


@api_view(['GET'])
def get_videos(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    data = []
    for video in videos:
        data.append({
            'id': video.id,
            'title': video.title,
            'status': video.status,
            'uploaded_at': video.uploaded_at,
        })
    return Response({'videos': data})