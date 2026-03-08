# Day 3 - Text to Image Generation

## Project: Cozy Cafe Coding Scene

### Objective
The goal of this exercise was to replicate the reference image of a young woman working on a laptop in a cozy cafe using prompt conditioning in a diffusion model. We aimed to produce a photorealistic image with consistent lighting, composition, and style.

---

### Prompt Used
**system_prompt.txt**


---

### SEED
70216

- The SEED ensures reproducibility of the generated image.  
- Keeping the SEED fixed while adjusting the prompt allows evaluation of prompt changes without random variations.

---

### Tools Used
- **Diffusion Model:** Stable Diffusion / Z-Image Turbo  
- **Platform:** [Hugging Face Spaces - Z-Image Turbo](https://huggingface.co/spaces/mrfakename/ZImage-Turbo)  
- **Camera/Style Emulation:** 50mm lens, shallow depth of field, photorealistic lighting

---

#
### Iterative Refinement Process

#### Step 1 - Initial Prompt
- **Prompt:** `"A woman in a cafe"`  
- **Observation:** Output lacked detail and atmosphere  
- **Output Image:**  
![Step 1](outputs/step1_initial.png)  

---

#### Step 2 - Composition Refinement
- **Prompt:** `"side profile, medium shot"` added  
- **Observation:** Improved framing and perspective  
- **Output Image:**  
![Step 2](outputs/step2_composition.png)  

---

#### Step 3 - Lighting & Style Refinement
- **Prompt:** `"soft natural window light, photorealistic, cinematic"` added  
- **Observation:** Enhanced realism, cozy warm mood  
- **Output Image:**  
![Step 3](outputs/step3_style_lighting.png)  

---

#### Step 4 - Final Output
- **Prompt:** Full combined prompt:  
```text
A young woman working on a laptop in a cozy cafe near a large window. She is sitting at a small round wooden table with a cup of coffee beside the laptop. The woman is wearing casual clothing and glasses while typing code on the laptop screen. Natural daylight is coming through the window, creating soft warm lighting. The background shows a calm modern cafe interior with blurred furniture and a relaxed atmosphere.

composition: side profile view, medium shot
environment: modern cafe interior, wooden table, coffee cup
lighting: soft natural window light, warm tones
style: realistic photography
camera: 50mm lens, shallow depth of field
quality: photorealistic, high detail, cinematic lighting

---

### Notes
- Changing the SEED generates alternative variations while keeping the prompt fixed.  
- Documenting prompt changes and SEED ensures reproducibility and supports fair "before vs after" comparisons.  
- This README captures the full iterative process from initial prompt to final output.