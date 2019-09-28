import Algorithmia

pen = "https://drive.google.com/open?id=1JhalujaLZ4NofxWdUnf_1cORV9zjFhpF"
landline = "https://drive.google.com/open?id=1JmCfuOHBGvswTyX5XyMxGIeKlpa7tBcu"
frooti = "https://drive.google.com/open?id=1JrrXow-sxMG2gQKvifmswEarNM-CSe_c"
phone = "https://drive.google.com/open?id=1Jt_glyxwvs2YldJXU_8L5YPj7kFKvP2f"
input = {
  "image": phone,
  #"output": "data://.algo/deeplearning/ObjectDetectionCOCO/temp/suit_and_tie.png",
  "min_score": 0.7,
  "model": "ssd_mobilenet_v1"
}
client = Algorithmia.client('simqB/07rMuzBQ+VsvXxmidtJhJ1')
algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.1')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)
