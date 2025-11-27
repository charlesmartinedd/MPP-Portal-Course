#!/usr/bin/env python3
"""
AI Voiceover Generation Script for MPP Portal Tour
Generates 50-second narration using Google Cloud TTS
"""

import os
import sys

# Voiceover script (50 seconds total)
VOICEOVER_SCRIPT = """
Welcome to the Mentor-Protégé Program Portal — your gateway to transformative defense contracting partnerships.

Mentors shape careers through subcontracting partnerships, networking opportunities, and earning credit toward small business goals.

Protégés receive guidance from prime contractors in business development, technical capabilities, and federal procurement with hands-on support.

Join the annual MPP Summit where mentors and protégés connect to build relationships and discover new collaboration opportunities.

Ready to get connected? Submit your information and our Program Office will guide you through the next steps.
"""

def generate_with_google_tts():
    """Generate audio using Google Cloud Text-to-Speech"""
    try:
        from google.cloud import texttospeech
        import io

        print("Using Google Cloud Text-to-Speech...")

        # Create client
        client = texttospeech.TextToSpeechClient()

        # Set voice parameters
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-J",  # Professional male voice
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )

        # Set audio config
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1.1,  # Slightly faster for 50s duration
            pitch=0.0,
            sample_rate_hertz=44100
        )

        # Synthesize
        synthesis_input = texttospeech.SynthesisInput(text=VOICEOVER_SCRIPT)
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Save audio
        output_path = os.path.join(os.path.dirname(__file__), "mpp-portal-voiceover.mp3")
        with open(output_path, "wb") as out:
            out.write(response.audio_content)

        print(f"Audio generated successfully: {output_path}")
        print(f"Size: {len(response.audio_content) / 1024:.1f} KB")
        return output_path

    except ImportError:
        print("Google Cloud TTS library not found. Install with: pip install google-cloud-texttospeech")
        return None
    except Exception as e:
        print(f"Error with Google TTS: {e}")
        return None

def generate_with_edge_tts():
    """Generate audio using Edge-TTS (free alternative)"""
    try:
        import edge_tts
        import asyncio

        print("Using Edge-TTS (Microsoft)...")

        async def generate_audio():
            voice = "en-US-GuyNeural"  # Professional male voice
            communicate = edge_tts.Communicate(VOICEOVER_SCRIPT, voice, rate="+10%")

            output_path = os.path.join(os.path.dirname(__file__), "mpp-portal-voiceover.mp3")
            await communicate.save(output_path)

            return output_path

        output_path = asyncio.run(generate_audio())
        print(f"Audio generated successfully: {output_path}")

        # Get file size
        size = os.path.getsize(output_path)
        print(f"Size: {size / 1024:.1f} KB")

        return output_path

    except ImportError:
        print("Edge-TTS library not found. Install with: pip install edge-tts")
        return None
    except Exception as e:
        print(f"Error with Edge-TTS: {e}")
        return None

def generate_with_gtts():
    """Generate audio using gTTS (fallback free option)"""
    try:
        from gtts import gTTS

        print("Using gTTS (Google Text-to-Speech - free)...")

        # Create TTS object
        tts = gTTS(text=VOICEOVER_SCRIPT, lang='en', slow=False, tld='com')

        # Save audio
        output_path = os.path.join(os.path.dirname(__file__), "mpp-portal-voiceover.mp3")
        tts.save(output_path)

        print(f"Audio generated successfully: {output_path}")

        # Get file size
        size = os.path.getsize(output_path)
        print(f"Size: {size / 1024:.1f} KB")

        return output_path

    except ImportError:
        print("gTTS library not found. Install with: pip install gtts")
        return None
    except Exception as e:
        print(f"Error with gTTS: {e}")
        return None

def save_script_only():
    """Save just the script text file"""
    output_path = os.path.join(os.path.dirname(__file__), "voiceover-script.txt")
    with open(output_path, 'w') as f:
        f.write(VOICEOVER_SCRIPT)
    print(f"Voiceover script saved to: {output_path}")
    print("\nScript content:")
    print("-" * 60)
    print(VOICEOVER_SCRIPT)
    print("-" * 60)
    return output_path

if __name__ == "__main__":
    print("MPP Portal Voiceover Generator")
    print("=" * 60)
    print(f"Target duration: ~50 seconds")
    print(f"Script length: {len(VOICEOVER_SCRIPT.split())} words")
    print("=" * 60)
    print()

    # Try different TTS methods in order of preference
    audio_path = None

    # Try Edge-TTS first (free, high quality)
    print("Attempting Edge-TTS...")
    audio_path = generate_with_edge_tts()

    # Try Google Cloud TTS if Edge-TTS failed
    if not audio_path:
        print("\nAttempting Google Cloud TTS...")
        audio_path = generate_with_google_tts()

    # Try gTTS as final fallback
    if not audio_path:
        print("\nAttempting gTTS...")
        audio_path = generate_with_gtts()

    # If all methods failed, save script for manual generation
    if not audio_path:
        print("\n⚠ All TTS methods failed. Saving script for manual generation.")
        print("You can use online services like:")
        print("- ElevenLabs: https://elevenlabs.io")
        print("- Google Cloud TTS: https://cloud.google.com/text-to-speech")
        print("- Amazon Polly: https://aws.amazon.com/polly/")
        save_script_only()
    else:
        print(f"\n✓ Voiceover generated successfully!")
        print(f"Next step: Convert to Base64 and embed in HTML")
