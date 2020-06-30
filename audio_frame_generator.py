import os
import json

env_file = open('env.json').read()
env = json.loads(env_file)
videoDeceptiveFileName = env['VIDEO_DECEPTIVE_FILE']
frameDeceptiveFileName = env['FRAME_DECEPTIVE_FILE']
audioDeceptiveFileName = env['AUDIO_DECEPTIVE_FILE']
videoTruthfulFileName = env['VIDEO_TRUTHFUL_FILE']
frameTruthfulFileName = env['FRAME_TRUTHFUL_FILE']
audioTruthfulFileName = env['AUDIO_TRUTHFUL_FILE']

os.system('mkdir ' + audioDeceptiveFileName)
os.system('mkdir ' + frameDeceptiveFileName)
for i in range(1,61):
    os.system('ffmpeg -i '+ videoDeceptiveFileName + '{0:03d}'.format(i) + '.mp4 -f mp3 -ab 75000 -vn '+ audioDeceptiveFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3')
    os.system('ffmpeg -i '+ audioDeceptiveFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3 -ac 1 '+ audioDeceptiveFileName + '/audio'+'{0:03d}'.format(i) +'.mp3')
    os.system('rm '+ audioDeceptiveFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3')
    os.system('mkdir ' + frameDeceptiveFileName + '/Frames' + '{0:03d}'.format(i))
    os.system('ffmpeg -i '+ videoDeceptiveFileName + '{0:03d}'.format(i) + '.mp4 -an -r 15 -s 60x40 '+ frameDeceptiveFileName + '/Frames' +'{0:03d}'.format(i) + '/frame%06d.jpg')

os.system('mkdir ' + audioTruthfulFileName)
os.system('mkdir ' + frameTruthfulFileName)
for i in range(1,61):
    os.system('ffmpeg -i '+ videoTruthfulFileName + '{0:03d}'.format(i) + '.mp4 -f mp3 -ab 75000 -vn '+ audioTruthfulFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3')
    os.system('ffmpeg -i '+ audioTruthfulFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3 -ac 1 '+ audioTruthfulFileName + '/audio'+'{0:03d}'.format(i) +'.mp3')
    os.system('rm '+ audioTruthfulFileName + '/audio'+'{0:03d}'.format(i) +'E.mp3')
    os.system('mkdir ' + frameTruthfulFileName + '/Frames' + '{0:03d}'.format(i))
    os.system('ffmpeg -i '+ videoTruthfulFileName + '{0:03d}'.format(i) + '.mp4 -an -r 15 -s 60x40 '+ frameTruthfulFileName + '/Frames' +'{0:03d}'.format(i) + '/frame%06d.jpg')
