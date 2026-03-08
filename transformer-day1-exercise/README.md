# Transformer Attention – Day 1 Exercise

This repository contains conceptual explanations and a simple implementation of the **Scaled Dot-Product Attention** mechanism used in Transformer models.  
The purpose of this exercise is to understand the fundamentals of **Generative AI, Self-Attention, and Vision Transformers**, and implement the core attention mechanism using **NumPy**.

This project is part of an **AI internship learning exercise** designed to test conceptual understanding, coding practices, and the ability to publish structured work on GitHub.

---

# Repository Structure

transformer-day1-exercise-imranashraf/

├── README.md  
├── attention_demo.py  
└── requirements.txt  

README.md – Conceptual explanations and documentation  
attention_demo.py – Implementation of scaled dot-product attention  
requirements.txt – Python dependency list

---

# What is Generative AI?

Generative AI is a type of artificial intelligence that can create new content like text, images, code, music, or videos. Unlike traditional machine learning models that mainly focus on prediction or classification, Generative AI produces new outputs based on patterns it has learned from large datasets.

For example, a traditional machine learning system might predict whether an email is spam or not. In contrast, a Generative AI model can write an email, generate an image, or create a piece of code.

Generative AI models learn patterns from massive datasets and then use those patterns to generate realistic outputs. These systems often rely on deep learning architectures such as **Transformers**, which are designed to process large sequences of data efficiently.

### Real-World Applications

**1. AI Chatbots**

Generative AI powers intelligent chatbots that can answer questions, assist users, and generate human-like conversations. These systems are used in customer support, education, and productivity tools.

**2. Image Generation**

Generative models can create images from text prompts. Designers and marketers use these systems to quickly generate visual concepts and artwork.

**3. Code Generation**

AI coding assistants help developers write code faster by suggesting functions, completing code snippets, and explaining programming concepts.

Generative AI is widely used in industries such as software development, marketing, healthcare, research, and content creation.

---

# Self-Attention Explained

Consider the sentence:

"The cat sat on the mat."

Self-attention allows a model to understand relationships between words in a sentence.

When the model processes the word **"sat"**, it needs to understand **who performed the action**. In this case, the word **"cat"** is the subject. Self-attention helps the model identify this relationship.

Instead of processing words one by one, the Transformer allows each word to **look at all other words in the sentence** and determine which ones are important.

---

## Query (Q), Key (K), and Value (V)

In the attention mechanism, each word is converted into three vectors:

**Query (Q)**  
Represents what the word is searching for.

**Key (K)**  
Represents the characteristics or identity of the word.

**Value (V)**  
Contains the information that will be passed forward to the next layer.

The model compares queries with keys to determine how strongly each word should attend to others. The resulting attention weights are then applied to the value vectors to produce the final output.

---

## Why do we scale by √dₖ ?

The dot product between query and key vectors can become very large when the vector dimension increases. Large values can make training unstable.

To prevent this, the scores are divided by the square root of the key dimension (√dₖ). This scaling keeps the values within a reasonable range and stabilizes the softmax calculation.

---

## Why apply Softmax?

Softmax converts raw attention scores into probabilities. This ensures that all attention weights add up to 1 and allows the model to determine which words are more important.

Example attention weights when processing the word **"sat"**:

Word | Attention Score  
cat  | 0.6  
sat  | 0.2  
mat  | 0.2  

This means the word **cat** contributes most to understanding the word **sat**.

---

## What problem does attention solve compared to RNNs?

Recurrent Neural Networks (RNNs) process words sequentially. When sentences become long, earlier information may be lost or weakened.

Self-attention solves this problem by allowing every word in the sentence to directly attend to every other word. This makes it easier for the model to capture long-range relationships and complex sentence structures.

---

# Encoder vs Decoder

Component | Encoder | Decoder  
--- | --- | ---  
Purpose | Understand input sequence | Generate output sequence  
Attention Type | Self-attention | Masked attention + cross-attention  
Input Access | Full input sequence | Only previously generated tokens  
Typical Use | Language understanding | Text generation  

---

## Masked Attention

Masked attention prevents the model from seeing future tokens during text generation.

Example:

The cat sat on the ___

The model must predict the next word without seeing the word **mat**, so future tokens are masked.

---

## Cross-Attention

Cross-attention allows the decoder to attend to the encoder's output.

This is commonly used in **machine translation**, where the decoder generates text in one language based on the encoded representation of another language.

---

# Vision Transformers (ViT)

Vision Transformers apply the Transformer architecture to image processing tasks.

Instead of processing the entire image at once, the image is divided into small sections called **patches**.

For example, an image of size **224 × 224 pixels** can be divided into **16 × 16 pixel patches**. Each patch is then flattened into a vector and converted into a token.

These tokens are processed by the Transformer in the same way that words are processed in natural language tasks.

However, Transformers do not inherently understand spatial order. Therefore, **positional embeddings** are added to each patch token. These embeddings help the model understand where each patch is located in the image.

This approach differs from traditional **Convolutional Neural Networks (CNNs)**. CNNs focus on detecting local patterns such as edges and textures, while Vision Transformers focus on relationships between patches across the entire image. This allows them to capture global context more effectively.

---

# Scaled Dot-Product Attention Formula

Attention(Q, K, V) = softmax((QKᵀ) / √dₖ) V

Where:

Q = Query matrix  
K = Key matrix  
V = Value matrix  
dₖ = Dimension of key vectors  

---

# Running the Attention Demo

Install dependencies:

pip install -r requirements.txt

Run the script:

python attention_demo.py

The script generates random Query, Key, and Value matrices and computes the scaled dot-product attention output.

---

# Example Output

Attention Output:

[[0.45 0.62 0.38 0.51]  
 [0.41 0.59 0.44 0.49]  
 [0.47 0.60 0.40 0.52]]

---

# Learning Objectives

This exercise demonstrates:

- Understanding of Generative AI concepts
- Conceptual knowledge of Transformer architecture
- Understanding of the Self-Attention mechanism
- Implementation of scaled dot-product attention using NumPy
- Writing clean and readable Python code

---

# References

Attention Is All You Need – Research Paper  
The Illustrated Transformer – Jay Alammar  
Vision Transformer Architecture Resources  
Generative AI Introductory Learning Materials