# Day 2 — Prompt Engineering & Text Generation

## Overview

This assignment focuses on **Prompt Engineering** for Large Language Models (LLMs).  
The goal is to design a structured prompt that can transform unstructured text feedback into a structured JSON output.

This exercise demonstrates how prompt design can guide AI models to produce **consistent, structured, and reliable responses**.

---

# Objective

Given a block of user feedback text, the AI model must generate a structured response containing:

- A concise **title**
- A **summary** (2–3 sentences)
- **Sentiment classification**
- Important **keywords**
- A **confidence score**

The output must strictly follow a **JSON format** so that it can easily be used in downstream applications.

---

# Prompt Engineering Approach

To ensure reliable outputs, the prompt follows these design principles:

### 1. Role Definition
The AI is assigned a clear role:

> AI assistant specialized in analyzing product feedback.

This helps guide the model toward relevant interpretations.

---

### 2. Clear Task Instructions

The prompt explicitly instructs the model to:

1. Read the feedback text carefully
2. Generate a concise title
3. Create a short summary
4. Detect sentiment
5. Extract meaningful keywords
6. Provide a confidence score

---

### 3. Strong Constraints

Constraints help reduce hallucinations and inconsistent outputs:

- Summary limited to **2–3 sentences**
- Sentiment must be **positive, negative, or neutral**
- Keywords must be **meaningful phrases**
- Confidence score must be **between 0.0 and 1.0**
- Output must be **valid JSON**

---

### 4. Structured Output

The output format is strictly enforced:

```json
{
"title": "string",
"summary": "string",
"sentiment": "positive | negative | neutral",
"keywords": ["string"],
"confidence_score": float
}
```

---

# System Prompt

The system prompt used for this assignment is stored in:

```
system_prompt.txt
```

This prompt instructs the model how to analyze and structure the response.

---

# Example Inputs and Outputs

## Example 1

### Input

The new update to the productivity app is impressive. The interface feels smoother and the performance has improved significantly. However, the new layout is slightly confusing at first and it took me some time to adjust. Overall, I think the update is a step in the right direction.

### Output

```json
{
"title": "Productivity App Update Improves Performance",
"summary": "The latest update improves performance and provides a smoother interface. Although the new layout may initially feel confusing, the overall update enhances the user experience.",
"sentiment": "positive",
"keywords": [
"productivity app",
"performance improvement",
"interface update",
"layout redesign",
"user experience"
],
"confidence_score": 0.87
}
```

---

## Example 2

### Input

The new version of the mobile banking app loads faster and the login process feels more secure. However, several features were moved to different sections, making it harder to find them.

### Output

```json
{
"title": "Mobile Banking App Update Improves Speed but Changes Navigation",
"summary": "The updated banking app offers faster performance and improved login security. However, the rearranged features make navigation slightly confusing for users.",
"sentiment": "neutral",
"keywords": [
"mobile banking app",
"performance improvement",
"security update",
"feature navigation",
"app redesign"
],
"confidence_score": 0.82
}
```

---

## Example 3

### Input

After the recent update, the photo editing app keeps crashing whenever I try to export images. The interface also feels slower than before and several tools are missing.

### Output

```json
{
"title": "Photo Editing App Update Causes Crashes and Missing Tools",
"summary": "The latest update introduces stability issues in the photo editing app. Users experience crashes during image export and slower interface performance.",
"sentiment": "negative",
"keywords": [
"photo editing app",
"app crashes",
"export failure",
"missing tools",
"performance issues"
],
"confidence_score": 0.91
}
```

---

# Key Learning Outcomes

This assignment demonstrates how prompt engineering can:

- Control the **structure of AI outputs**
- Improve **response consistency**
- Reduce **model hallucinations**
- Enable **machine-readable results**

Prompt engineering is a critical skill for building **AI-powered production systems**, especially when structured data outputs are required.

---

# Conclusion

By carefully designing prompts with:

- Defined roles
- Clear instructions
- Strong constraints
- Structured outputs

we can significantly improve the reliability of Large Language Model responses.

This assignment demonstrates a practical example of **reverse prompt engineering and structured AI response generation**.

---

---
