from ntpath import isdir
import os
from typing import final
from nudenet import NudeDetector
from make_images_from_video import make_images_from_video

def classify_images_dnpy(original_video_path, images_path = 'output/images', model_path = 'mobilenet_v2_140_224/saved_model.h5'):
    # final_images_path = make_images_from_video(original_video_path, images_path, save=True)
    final_images_path = '/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output/images'
    nude_detector = NudeDetector()
    # Walk through each file in the directory
    scenes_with_info = []
    file_paths = os.listdir(final_images_path)
    print(f"Found {len(file_paths)} files")
    file_paths = ['/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output/images/frame29870.jpg']
    for index, filename in enumerate(file_paths):
        # Is filename an absolute path?
        if index % 100 == 0:
            print(f"Processed {index} files out of {len(file_paths)}")
        if not os.path.isabs(filename):
            filename = os.path.join(final_images_path, filename)
        if os.path.isdir(filename):
            continue
        # The browser version gives back everything we expect, but running it here gives nothing, but should give multiple...
        result = nude_detector.detect(filename)
        if len(result) > 0:
            scenes_with_info.append(dict(file=filename, result=result))
    print(f"Found {len(scenes_with_info)} scenes that need analyzing")
    print(list(set(list(map(lambda x: ",".join(list(map(lambda y: y['class'], x['result']))), scenes_with_info)))))
    potential_bad_scenes = [x for x in list(filter(lambda x: len(list(filter(lambda y: y['class'] != 'FACE_FEMALE' and y['class'] != 'FACE_MALE', x['result']))) > 0, scenes_with_info)) if len(x) > 0]
    print(f"Found {len(potential_bad_scenes)} scenes that might be bad scenes, but checking scores")
    print(potential_bad_scenes)
    scenes_with_high_score = [scene for scene in potential_bad_scenes if len(list(filter(lambda x: x['score'] > 0.7, scene['result']))) > 0]
    print(f"Found {len(scenes_with_high_score)} bad scenes with a score more than 0.7")
    print(scenes_with_high_score)

if __name__ == "__main__":
    classify_images_dnpy('Thor The Dark World (2013).mkv')
