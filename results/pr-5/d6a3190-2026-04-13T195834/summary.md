# Test Results: PR #5

- **PR:** [pcuenca/mlx-lm#5](https://github.com/pcuenca/mlx-lm/pull/5)
- **Branch:** `olmo-hybrid-v2`
- **Commit:** [`d6a3190ce8105be98ec41471d90fe16f7c149b9f`](https://github.com/pcuenca/mlx-lm/commit/d6a3190ce8105be98ec41471d90fe16f7c149b9f)
- **Model type:** `olmo_hybrid`
- **Timestamp:** 2026-04-13T18:04:20+00:00

## Numerical comparison (transformers vs MLX)

| Variant | Max diff | Mean diff | <0.01 | <0.1 | Top-1 | Top-5 | Top-10 |
|---|---|---|---|---|---|---|---|
| `allenai/Olmo-Hybrid-7B` | 0.462723 | 0.065116 | 9.70% | 78.88% | True | 5/5 | 10/10 |
| `allenai/Olmo-Hybrid-Instruct-SFT-7B` | 0.283730 | 0.053892 | 11.27% | 86.60% | True | 5/5 | 10/10 |

## allenai/Olmo-Hybrid-7B

### dtype — PASS

<details><summary>stdout</summary>

```
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
```
</details>

### generate — ran

<details><summary>stdout</summary>

```
==========
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that were previously inaccessible to us.

One of the most exciting applications of gravitational wave astronomy is the study of the early universe, specifically the epoch known as the "Big Bang." This is the moment in time when the universe began, and it is believed to have occurred approximately 13.8 billion years ago. During this time, the universe was incredibly hot and dense, and it underwent a rapid expansion known as inflation. This inflationary period is thought to have lasted for a fraction of a second, but it had a profound impact on the structure and evolution of the universe.

One of the key predictions of inflationary theory is the existence of primordial gravitational waves. These are ripples in the fabric of spacetime that were generated during the inflationary period and have left an imprint on the cosmic microwave background radiation (CMB). The CMB is the afterglow of the Big Bang, and it provides us with
==========
Prompt: 57 tokens, 462.485 tokens-per-sec
Generation: 200 tokens, 43.154 tokens-per-sec
Peak memory: 15.047 GB
```
</details>

### long_sequence — ran

<details><summary>stdout</summary>

```
==========
The tutorial should be divided into 5 Sections, each marked with Section N, and each section should contain at least 3 paragraphs. Repeat your response in Spanish language as well.

**Section 1: Introduction to Web Servers**

A web server is a software application that processes requests made over the internet. It receives requests from clients, processes them, and sends back responses. The most common protocol used for web servers is HTTP (Hypertext Transfer Protocol). Understanding the basics of how web servers work is crucial for anyone looking to develop web applications.

Web servers operate by listening on a specific port for incoming requests. When a request is received, the server processes it and sends back a response. This response can be a simple acknowledgment or a full HTML page. The server's role is to interpret the request, process it, and send back the appropriate response.

One of the key components of a web server is its ability to handle multiple requests simultaneously. This is achieved through multithreading or asynchronous programming techniques. By handling multiple requests at once, the server can efficiently manage its resources and provide quick responses to users.

**Section 2: Setting Up the Environment**

Before diving into the code, it's essential to set up the development environment. This involves installing Python and setting up a virtual environment to isolate the project dependencies. Using a virtual environment helps manage dependencies and ensures that the project can be easily replicated on different systems.

Once the environment is set up, the next step is to install the necessary libraries. For a basic web server, libraries like `socketserver` and `http.server` from the Python standard library can be used. These libraries provide the necessary tools to handle HTTP requests and responses.

**Section 3: Implementing HTTP Requests**

The core of a web server is its ability to handle HTTP requests. This involves parsing the request headers, extracting the requested resource, and sending back the appropriate response. The server must be able to handle different types of requests, such as GET, POST, and others.

To handle requests, the server must parse the request headers to extract the requested resource. This involves reading the request line, headers, and body. The server must then determine the appropriate response based on the request type and content.

**Section 4: Handling Requests and Responses**

Handling requests and responses involves parsing the request headers and body, determining the appropriate response, and sending it back to the client. This involves parsing the request headers to extract the requested resource, determining the appropriate response based on the request type and content, and sending the response back to the client.

**Section 5: Error Handling and Logging**

Error handling and logging are crucial components of any web server. Proper error handling ensures that the server can gracefully handle unexpected errors and provide meaningful error messages to the client. Logging helps in debugging and monitoring the server's performance and behavior.

In conclusion, building a web server from scratch is a valuable exercise that provides a deep understanding of how web servers work. By following the steps outlined in this tutorial, you can gain a deeper understanding of how web servers work and how they process requests and responses.

---

**Section 1: Introducción**

Un servidor web es un programa que se ejecuta en un sistema operativo y se utiliza para proporcionar servicios a través de la red. Los servidores web se utilizan para proporcionar servicios web, como páginas web, aplicaciones web y servicios web de aplicaciones. Los servidores web se utilizan para proporcionar servicios web, como páginas web, aplicaciones web y servicios web de aplicaciones.

**Section 2: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración incluye la configuración de la base de datos, la configuración de la red y la configuración de la aplicación. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente. La configuración de la aplicación es importante para asegurar que la aplicación funcione correctamente.

**Section 3: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 4: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 5: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 6: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 7: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 8: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 9: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 10: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 11: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 12: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 13: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 14: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 15: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 16: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 17: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 18: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 19: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 20: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 21: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 22: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 23: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 24: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 25: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 26: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 27: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 28: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 29: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 30: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 31: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 32: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 33: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 34: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 35: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 36: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 37: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 38: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 39: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 40: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 41: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 42: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 43: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 44: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 45: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 46: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 47: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 48: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos es importante para asegurar que la aplicación funcione correctamente. La configuración de la red es importante para asegurar que la aplicación funcione correctamente.

**Section 49: Configuración de la aplicación**

La configuración de la aplicación es un proceso importante para asegurar que la aplicación funcione correctamente. La configuración de la base de datos
==========
Prompt: 26 tokens, 224.812 tokens-per-sec
Generation: 4096 tokens, 41.963 tokens-per-sec
Peak memory: 15.526 GB
```
</details>

### predictions — ran

<details><summary>stdout</summary>

```
=== TRANSFORMERS vs MLX COMPARISON ===
Model: allenai/Olmo-Hybrid-7B
Prompt: 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences'

Loading transformers model...
Loading MLX model...

Tokens (HF):  [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13, 1115, 11914, 5727, 1475, 6661, 315, 279, 6498, 28890, 520, 3325, 3131, 323, 706, 1027, 1511, 439, 264, 20061, 10368, 369, 927, 264, 9478, 13, 763, 279, 1917, 315, 25213, 11, 97974, 95801, 1093, 420, 832, 8854, 264, 15325, 7580, 7953, 17983, 62468, 13, 2435, 1520, 1296, 34080, 11, 71402, 11, 323, 1495, 21568, 6067, 555, 51582, 279, 2539, 2134, 315, 5885, 430, 264, 1887, 2011, 1862, 13, 22196, 23719]
Tokens (MLX): [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13, 1115, 11914, 5727, 1475, 6661, 315, 279, 6498, 28890, 520, 3325, 3131, 323, 706, 1027, 1511, 439, 264, 20061, 10368, 369, 927, 264, 9478, 13, 763, 279, 1917, 315, 25213, 11, 97974, 95801, 1093, 420, 832, 8854, 264, 15325, 7580, 7953, 17983, 62468, 13, 2435, 1520, 1296, 34080, 11, 71402, 11, 323, 1495, 21568, 6067, 555, 51582, 279, 2539, 2134, 315, 5885, 430, 264, 1887, 2011, 1862, 13, 22196, 23719]

============================================================
NUMERICAL COMPARISON
============================================================

Shape - HF: (1, 80, 100352), MLX: (1, 80, 100352)

HF logits  - min: -37.4794, max: 13.1810, mean: -14.9944, std: 5.9023
MLX logits - min: -37.2500, max: 13.1875, mean: -14.9508, std: 5.8926

Absolute diff - min: 0.000000, max: 0.462723, mean: 0.065116
Relative diff - min: 0.000000, max: 2749.174805, mean: 0.008953

Tolerance checks (% of values within threshold):
  < 0.001: 0.97%
  < 0.01: 9.70%
  < 0.1: 78.88%
  < 1.0: 100.00%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      3073       ' exist'             0.214905   3073       ' exist'             0.205766  
2      617        ' have'              0.190557   617        ' have'              0.193299  
3      649        ' can'               0.169736   649        ' can'               0.165337  
4      527        ' are'               0.087119   527        ' are'               0.091308  
5      11         ','                  0.078129   11         ','                  0.080579  
6      304        ' in'                0.045007   304        ' in'                0.047370  
7      1101       ' also'              0.036058   1101       ' also'              0.036892  
8      2663       ' called'            0.012976   2663       ' called'            0.013361  
9      5101       ' appear'            0.011175   5101       ' appear'            0.011251  
10     477        ' or'                0.009946   477        ' or'                0.010086  

============================================================
OVERLAP ANALYSIS
============================================================

Top-1 match: True
  HF:  3073 (' exist')
  MLX: 3073 (' exist')

Top-5 overlap: 5/5
  HF:  [np.int64(3073), np.int64(617), np.int64(649), np.int64(527), np.int64(11)]
  MLX: [np.int64(3073), np.int64(617), np.int64(649), np.int64(527), np.int64(11)]

Top-10 overlap: 10/10

============================================================
SUMMARY
============================================================
SUCCESS: Predictions match well
```
</details>

### quant_dtype — PASS

<details><summary>stdout</summary>

```
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
```
</details>

### quant_generate — ran

<details><summary>stdout</summary>

```
==========
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that were previously inaccessible to us.

One of the most exciting applications of gravitational wave astronomy is the study of the early universe, specifically the epoch known as the "cosmic dawn." This period marks the transition from the dark ages of the universe, when it was filled with neutral hydrogen gas, to the era of star formation and galaxy evolution. During this time, the first stars and galaxies formed, and their light began to illuminate the cosmos. However, the process of star formation is complex and poorly understood, and the details of how it occurred remain shrouded in mystery.

One of the key challenges in studying the early universe is the fact that the universe was opaque during this time, making it difficult to observe directly. However, gravitational waves offer a unique window into this era, as they can penetrate the opaque universe and provide a direct view of the early cosmos. By studying the gravitational waves emitted during the early universe,
==========
Prompt: 57 tokens, 549.467 tokens-per-sec
Generation: 200 tokens, 107.148 tokens-per-sec
Peak memory: 4.455 GB
```
</details>

### quantize — ran

<details><summary>stdout</summary>

```
[INFO] Loading
[INFO] Quantizing
[INFO] Quantized model with 4.502 bits per weight.
```
</details>

## allenai/Olmo-Hybrid-Instruct-SFT-7B

### dtype — PASS

<details><summary>stdout</summary>

```
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
```
</details>

### generate — ran

<details><summary>stdout</summary>

```
==========
A transformer neural network is a type of deep learning model that is widely used for natural language processing (NLP) tasks such as language translation, text summarization, and sentiment analysis. Here is a step-by-step explanation of how a transformer processes a sentence:

1. Tokenization: The input sentence is first tokenized into individual words or subwords. This is done using a tokenizer, which is a pre-trained model that has been trained on a large corpus of text.

2. Embedding: Each token is then converted into a dense vector representation using an embedding layer. The embedding layer is trained on a large corpus of text and learns to represent each word in a high-dimensional vector space.

3. Positional Encoding: Since the order of words in a sentence is important, the transformer model uses positional encoding to encode the position of each word in the sentence. This is done by adding a positional encoding vector to each word's embedding vector.

4. Self-Attention: The transformer model uses self
==========
Prompt: 51 tokens, 413.082 tokens-per-sec
Generation: 200 tokens, 42.994 tokens-per-sec
Peak memory: 15.038 GB
```
</details>

### long_sequence — ran

<details><summary>stdout</summary>

```
==========
Creating a full Space Invaders game in HTML and JavaScript is a complex task that involves a lot of code. However, I can provide you with a basic structure of how you might start to build this game. This will include the HTML structure, JavaScript for the game logic, and CSS for the styling.

HTML:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Space Invaders</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <script src="game.js"></script>
</body>
</html>
```

CSS (style.css):
```css
body {
    background-color: #000;
    color: #fff;
}

#gameCanvas {
    background-color: #000;
    border: 1px solid #000;
}
```

JavaScript (game.js):
```javascript
var canvas = document.getElementById('gameCanvas');
var ctx = canvas.getContext('2d');

var player = {
    x: 100,
    y: 500,
    width: 50,
    height: 50,
    speed: 5
};

var alien = {
    x: 200,
    y: 50,
    width: 50,
    height: 50,
    speed: 3
};

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPlayer();
    drawAlien();
    drawBullets();
}

function drawPlayer() {
    ctx.fillStyle = 'blue';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawAlien() {
    ctx.fillStyle = 'red';
    ctx.fillRect(alien.x, alien.y, alien.width, alien.height);
}

function drawBullets() {
    ctx.fillStyle = 'white';
    ctx.fillRect(100, 500, 50, 50);
}

setInterval(draw, 10);
```

This is a very basic implementation of the game. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every 10 milliseconds. The player and the alien are drawn on the canvas, and the game loop is run every
==========
Prompt: 49 tokens, 400.724 tokens-per-sec
Generation: 4096 tokens, 42.042 tokens-per-sec
Peak memory: 15.525 GB
```
</details>

### predictions — ran

<details><summary>stdout</summary>

```
=== TRANSFORMERS vs MLX COMPARISON ===
Model: allenai/Olmo-Hybrid-Instruct-SFT-7B
Prompt: 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences'

Loading transformers model...
Loading MLX model...

Tokens (HF):  [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13, 1115, 11914, 5727, 1475, 6661, 315, 279, 6498, 28890, 520, 3325, 3131, 323, 706, 1027, 1511, 439, 264, 20061, 10368, 369, 927, 264, 9478, 13, 763, 279, 1917, 315, 25213, 11, 97974, 95801, 1093, 420, 832, 8854, 264, 15325, 7580, 7953, 17983, 62468, 13, 2435, 1520, 1296, 34080, 11, 71402, 11, 323, 1495, 21568, 6067, 555, 51582, 279, 2539, 2134, 315, 5885, 430, 264, 1887, 2011, 1862, 13, 22196, 23719]
Tokens (MLX): [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13, 1115, 11914, 5727, 1475, 6661, 315, 279, 6498, 28890, 520, 3325, 3131, 323, 706, 1027, 1511, 439, 264, 20061, 10368, 369, 927, 264, 9478, 13, 763, 279, 1917, 315, 25213, 11, 97974, 95801, 1093, 420, 832, 8854, 264, 15325, 7580, 7953, 17983, 62468, 13, 2435, 1520, 1296, 34080, 11, 71402, 11, 323, 1495, 21568, 6067, 555, 51582, 279, 2539, 2134, 315, 5885, 430, 264, 1887, 2011, 1862, 13, 22196, 23719]

============================================================
NUMERICAL COMPARISON
============================================================

Shape - HF: (1, 80, 100352), MLX: (1, 80, 100352)

HF logits  - min: -35.6609, max: 7.6640, mean: -17.3078, std: 4.6833
MLX logits - min: -35.5000, max: 7.7812, mean: -17.2724, std: 4.6901

Absolute diff - min: 0.000000, max: 0.283730, mean: 0.053892
Relative diff - min: 0.000000, max: 51.743309, mean: 0.003586

Tolerance checks (% of values within threshold):
  < 0.001: 1.13%
  < 0.01: 11.27%
  < 0.1: 86.60%
  < 1.0: 100.00%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      617        ' have'              0.284796   617        ' have'              0.285077  
2      304        ' in'                0.192666   304        ' in'                0.191392  
3      3073       ' exist'             0.143044   3073       ' exist'             0.144470  
4      527        ' are'               0.068259   527        ' are'               0.070272  
5      11         ','                  0.057079   11         ','                  0.056644  
6      649        ' can'               0.025840   649        ' can'               0.026516  
7      1051       ' were'              0.024295   1051       ' were'              0.024813  
8      5101       ' appear'            0.017901   5101       ' appear'            0.017802  
9      449        ' with'              0.017404   449        ' with'              0.016724  
10     505        ' from'              0.016584   505        ' from'              0.016083  

============================================================
OVERLAP ANALYSIS
============================================================

Top-1 match: True
  HF:  617 (' have')
  MLX: 617 (' have')

Top-5 overlap: 5/5
  HF:  [np.int64(617), np.int64(304), np.int64(3073), np.int64(527), np.int64(11)]
  MLX: [np.int64(617), np.int64(304), np.int64(3073), np.int64(527), np.int64(11)]

Top-10 overlap: 10/10

============================================================
SUMMARY
============================================================
SUCCESS: Predictions match well
```
</details>

### quant_dtype — PASS

<details><summary>stdout</summary>

```
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
```
</details>

### quant_generate — ran

<details><summary>stdout</summary>

```
==========
A transformer neural network processes a sentence by encoding the input into a sequence of vectors, then using self-attention mechanisms to weigh the importance of each word in the sentence. The output is a sequence of vectors that can be used for a variety of tasks, such as translation or sentiment analysis.
==========
Prompt: 51 tokens, 484.163 tokens-per-sec
Generation: 59 tokens, 107.997 tokens-per-sec
Peak memory: 4.439 GB
```
</details>

### quantize — ran

<details><summary>stdout</summary>

```
[INFO] Loading
[INFO] Quantizing
[INFO] Quantized model with 4.502 bits per weight.
```
</details>

## Notes

DPO variant uses NoPE (rope_theta: null) while base/SFT/Think-SFT use RoPE with theta=10000. The numerical comparison at 100+ tokens should catch any RoPE misconfiguration across variants.

