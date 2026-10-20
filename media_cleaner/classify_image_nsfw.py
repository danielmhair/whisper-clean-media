import os
from nsfw_detector import predict
from make_images_from_video import make_images_from_video

def classify_images_nsfw(original_video_path, images_path = 'output/images', model_path = 'mobilenet_v2_140_224/saved_model.h5'):
    final_images_path = make_images_from_video(original_video_path, images_path)
    model_path = os.path.join(os.path.dirname(__file__), model_path)
    model = predict.load_model(model_path)
    result = predict.classify(model, final_images_path)
    def lambda_a(a):
        result[a]['path'] = a
        return result[a]
    next_result = list(map(lambda_a, sorted(result.keys(), key=lambda x: (result[x]['porn'], result[x]['sexy']), reverse=True)))
    print(next_result)

if __name__ == "__main__":
    classify_images_nsfw('Ghostbusters (1984).mkv')
