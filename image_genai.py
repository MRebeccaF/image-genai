# -*- coding: utf-8 -*-
"""image_genai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lMukzu8kKWoRqUzbAnHz4WiOLlvlfjUB
"""

# Installing the required libraries
!pip install diffusers transformers torch accelerate safetensors

from diffusers import StableDiffusionPipeline
import torch

# Loading pre-trained Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"  # You can choose other versions if needed
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Move the pipeline to GPU for faster inference
pipe = pipe.to("cuda")

# Define your text prompt
prompt = input("Enter your text prompt: ")
h=800
w=600
steps=25
guidance=7.5
# Generate the image
image = pipe(prompt).images[0]

# Display the generated image
image

