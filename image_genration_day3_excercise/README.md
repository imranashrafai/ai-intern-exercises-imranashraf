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

### Iterative Refinement Process
| Step | Prompt Modification | Observations |
|------|-------------------|-------------|
| 1 | "A woman in a cafe" | Output lacked detail and atmosphere |
| 2 | Added composition: "side profile, medium shot" | Improved framing and perspective |
| 3 | Added lighting & style: "soft natural window light, photorealistic, cinematic" | Enhanced realism, cozy warm mood |
| 4 | Final prompt with all modifiers + SEED 70216 | Achieved closest match to reference image |

**Intermediate Outputs:**  
- `step1_initial.png` – baseline scene  
- `step2_composition.png` – framing refined  
- `step3_style_lighting.png` – lighting and photorealism refined  

---

### Final Output
- **File:** `final_image.png`  
- Generated using the final prompt and SEED 70216  
- Represents the best reproduction of the reference image with photorealistic details


### Final Image
![Final generated image](final_image.png)

### Iterative Steps

#### Step 1 - Initial Prompt
![Step 1](step1_initial.png)

#### Step 2 - Composition Refinement
![Step 2](step2_composition.png)

---

### Notes
- Changing the SEED generates alternative variations while keeping the prompt fixed.  
- Documenting prompt changes and SEED ensures reproducibility and supports fair "before vs after" comparisons.  
- This README captures the full iterative process from initial prompt to final output.