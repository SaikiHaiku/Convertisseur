#!/usr/bin/env python3
import shutil
import subprocess
import sys
from pathlib import Path




def check_ffmpeg():
if not shutil.which('ffmpeg'):
raise RuntimeError('ffmpeg not found in PATH')




def run_ffmpeg(cmd_args):
print('Running:', ' '.join(cmd_args))
p = subprocess.run(cmd_args)
if p.returncode != 0:
raise RuntimeError(f"ffmpeg failed with code {p.returncode}")




def build_cmd(input_path, output_path, args):
cmd = ['ffmpeg', '-y', '-i', str(input_path)]


# Audio options
if args.audio_bitrate:
cmd += ['-b:a', args.audio_bitrate]
if args.audio_codec:
cmd += ['-c:a', args.audio_codec]


# Video options
if args.video_codec:
cmd += ['-c:v', args.video_codec]
if args.video_bitrate:
cmd += ['-b:v', args.video_bitrate]
if args.scale:
cmd += ['-vf', f'scale={args.scale}']


# If output is audio-only container, force removal of video stream
ext = output_path.suffix.lower()
audio_only_exts = {'.mp3', '.aac', '.m4a', '.wav', '.flac', '.ogg', '.opus'}
if ext in audio_only_exts:
cmd += ['-vn']


cmd.append(str(output_path))
return cmd




def main():
parser = argparse.ArgumentParser()
parser.add_argument('input', type=Path)
parser.add_argument('output', type=Path)
parser.add_argument('--audio-bitrate', type=str, default=None)
parser.add_argument('--video-bitrate', type=str, default=None)
parser.add_argument('--scale', type=str, default=None, help='e.g. 1280:720 or -1:720')
parser.add_argument('--audio-codec', type=str, default=None)
parser.add_argument('--video-codec', type=str, default=None)


args = parser.parse_args()


check_ffmpeg()


if not args.input.exists():
print('Input file not found:', args.input, file=sys.stderr)
sys.exit(2)


cmd = build_cmd(args.input, args.output, args)
run_ffmpeg(cmd)
print('Conversion terminée:', args.output)




if __name__ == '__main__':
main()
