# Test Results: PR #5

- **PR:** [pcuenca/mlx-lm#5](https://github.com/pcuenca/mlx-lm/pull/5)
- **Branch:** `olmo-hybrid-v2`
- **Commit:** [`b0706fc8f6125a85372d1096345604a88b20d300`](https://github.com/pcuenca/mlx-lm/commit/b0706fc8f6125a85372d1096345604a88b20d300)
- **Model type:** `olmo_hybrid`
- **Timestamp:** 2026-04-13T18:15:12+00:00

## Numerical comparison (transformers vs MLX)

| Variant | Max diff | Mean diff | <0.01 | <0.1 | Top-1 | Top-5 | Top-10 |
|---|---|---|---|---|---|---|---|
| `allenai/Olmo-Hybrid-7B` | 3.923443 | 0.412041 | 2.67% | 25.32% | True | 4/5 | 9/10 |
| `allenai/Olmo-Hybrid-Instruct-SFT-7B` | 4.580130 | 0.516765 | 1.77% | 18.46% | True | 5/5 | 8/10 |

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
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that occurred during the first moments after the Big Bang.

One of the most exciting applications of gravitational wave astronomy is the search for primordial gravitational waves, which are believed to have been generated during the inflationary epoch of the universe. During this period, the universe underwent an exponential expansion, stretching out to its current size in a fraction of a second. It is thought that this rapid expansion may have generated a background of gravitational waves, which could provide valuable information about the nature of the inflationary process and the conditions that existed in the early universe.

The detection of primordial gravitational waves would be a major breakthrough in our understanding of the universe, as it would provide direct evidence for the inflationary model of cosmology. However, detecting these waves is a challenging task, as they are extremely faint and difficult to distinguish from other sources of noise. Nevertheless, several experiments are currently underway to search for primordial gravitational waves, including
==========
Prompt: 57 tokens, 455.254 tokens-per-sec
Generation: 200 tokens, 43.191 tokens-per-sec
Peak memory: 15.041 GB
```
</details>

### long_sequence — ran

<details><summary>stdout</summary>

```
==========
The tutorial should be divided into 5 Sections, each marked with Section N, and each section should contain at least 3 paragraphs. Repeat your response in Spanish language as well.

**Section 1: Introduction to Web Servers and Sockets**

Building a web server from scratch is an excellent way to understand the fundamental concepts of how the internet works. A web server is a software application that serves content to clients over the internet. The first step in creating a web server is to understand how it communicates with clients using sockets. Sockets are endpoints for sending and receiving data across a network. In Python, the `socket` module provides the necessary tools to create and manage these connections.

To start, you need to import the `socket` module and create a socket object. This object will act as the server's endpoint for accepting connections from clients. The server socket is typically bound to a specific IP address and port number, which clients will use to connect to the server. Once the server socket is created, it enters a listening state, waiting for incoming connections. When a client attempts to connect, the server accepts the connection, creating a new socket for the communication between the server and the client.

Understanding how to handle these connections is crucial. The server must be able to accept multiple connections simultaneously, which is where the concept of a thread pool or asynchronous programming comes into play. By using threads or asynchronous methods, the server can handle multiple clients without blocking, ensuring efficient communication. This section sets the foundation for understanding how a web server interacts with clients over a network, using sockets as the primary means of communication.

**Section 2: HTTP Parsing and Request Handling**

Once the server is set up to accept connections, the next step is to parse HTTP requests. HTTP, or Hypertext Transfer Protocol, is the foundation of data communication on the World Wide Web. When a client sends a request to the server, it follows a specific format that the server must parse to understand the client's intent. This involves reading the request line, headers, and body of the HTTP request.

Parsing an HTTP request involves breaking down the request into its components. The request line contains the HTTP method (GET, POST, etc.), the requested resource, and the HTTP version. The headers provide additional information about the request, such as the client's user agent, accepted content types, and more. The body of the request may contain data being sent to the server, such as form data or uploaded files. Understanding how to parse these components is essential for processing the request correctly.

After parsing the request, the server must determine how to handle it. This involves routing the request to the appropriate handler based on the requested resource. For example, if the request is for a specific file, the server should serve that file. If the request is for a dynamic resource, such as a script, the server should execute the script and return the output. Properly handling HTTP requests is crucial for ensuring that the server responds appropriately to client requests.

**Section 3: Routing and URL Mapping**

Routing is a critical component of a web server, as it determines how requests are handled based on the requested URL. URL mapping involves associating specific URLs with corresponding handlers or functions. This allows the server to direct requests to the appropriate code based on the URL path. Effective URL mapping ensures that the server can handle a wide range of requests efficiently.

To implement URL mapping, you can use a dictionary or a more complex routing system that maps URL patterns to handler functions. For example, you might map the root URL to a function that serves the homepage, while other URLs map to functions that handle specific resources or actions. This approach allows for flexibility and scalability, as new routes can be added without modifying existing code.

In addition to mapping URLs to handlers, it's important to consider how to handle dynamic content. Dynamic content is generated on the fly based on user input or other factors. This often involves using templates or rendering engines to generate HTML content dynamically. By combining URL mapping with dynamic content generation, the server can provide a rich and interactive user experience.

**Section 4: Error Handling and Logging**

Error handling is an essential aspect of building a robust web server. Errors can occur at various stages of request processing, from parsing the request to executing the handler. Proper error handling ensures that the server can gracefully manage unexpected situations and provide meaningful feedback to clients. This involves implementing try-except blocks, logging errors, and returning appropriate HTTP status codes.

Logging is a crucial part of error handling, as it allows you to track issues and diagnose problems. By logging errors and warnings, you can gain insights into the server's behavior and identify areas for improvement. Logging should be configured to write to a file or a logging service, ensuring that logs are retained and accessible for analysis.

In addition to logging, the server should return appropriate HTTP status codes in response to errors. For example, if a requested resource is not found, the server should return a 404 Not Found status code. Similarly, if there is an internal server error, a 500 Internal Server Error status code should be returned. Proper error handling and logging contribute to a reliable and user-friendly web server.

**Section 5: Security Considerations**

Security is a paramount concern when building a web server. Ensuring that the server is secure involves implementing measures to protect against common vulnerabilities, such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF). These vulnerabilities can be exploited by malicious actors to gain unauthorized access to the server or manipulate data.

One of the first steps in securing a web server is to validate and sanitize user input. This involves checking that input data conforms to expected formats and removing any potentially harmful characters. Additionally, using prepared statements for database queries can prevent SQL injection attacks by ensuring that user input is treated as data rather than executable code.

Another important security consideration is authentication and authorization. Implementing secure authentication mechanisms, such as OAuth or JWT, ensures that only authorized users can access certain resources. Additionally, role-based access control (RBAC) can be used to restrict access to sensitive data based on user roles.

Finally, regular security audits and updates are essential for maintaining a secure web server. Keeping the server software and dependencies up to date ensures that known vulnerabilities are patched promptly. By prioritizing security, you can build a web server that is both functional and secure, providing a safe environment for users and data.
==========
Prompt: 26 tokens, 226.969 tokens-per-sec
Generation: 1300 tokens, 40.050 tokens-per-sec
Peak memory: 15.139 GB
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
MLX logits - min: -37.7500, max: 13.0625, mean: -15.0156, std: 6.0261

Absolute diff - min: 0.000000, max: 3.923443, mean: 0.412041
Relative diff - min: 0.000000, max: 5829.320801, mean: 0.050857

Tolerance checks (% of values within threshold):
  < 0.001: 0.27%
  < 0.01: 2.67%
  < 0.1: 25.32%
  < 1.0: 89.25%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      3073       ' exist'             0.214905   3073       ' exist'             0.348988  
2      617        ' have'              0.190557   617        ' have'              0.159778  
3      649        ' can'               0.169736   649        ' can'               0.124435  
4      527        ' are'               0.087119   11         ','                  0.068720  
5      11         ','                  0.078129   304        ' in'                0.062570  
6      304        ' in'                0.045007   527        ' are'               0.053519  
7      1101       ' also'              0.036058   1101       ' also'              0.022310  
8      2663       ' called'            0.012976   2663       ' called'            0.019383  
9      5101       ' appear'            0.011175   477        ' or'                0.011218  
10     477        ' or'                0.009946   449        ' with'              0.010539  

============================================================
OVERLAP ANALYSIS
============================================================

Top-1 match: True
  HF:  3073 (' exist')
  MLX: 3073 (' exist')

Top-5 overlap: 4/5
  HF:  [np.int64(3073), np.int64(617), np.int64(649), np.int64(527), np.int64(11)]
  MLX: [np.int64(3073), np.int64(617), np.int64(649), np.int64(11), np.int64(304)]

Top-10 overlap: 9/10

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
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that occurred when the universe was only a fraction of a second old. This has led to a renewed interest in the study of the early universe, with researchers now able to probe the very first moments of cosmic history in ways that were previously impossible.
The discovery of gravitational waves has also had a significant impact on our understanding of the nature of black holes. Prior to the discovery, we had only indirect evidence for the existence of black holes, based on their effects on surrounding matter. However, the detection of gravitational waves from merging black holes has provided direct evidence for their existence, as well as providing new insights into their properties. For example, the detection of gravitational waves from the merger of two black holes has allowed us to measure the mass and spin of the black holes involved, providing a new way to study these enigmatic objects.
The discovery of gravitational waves has also had a profound impact on our understanding of the nature of the
==========
Prompt: 57 tokens, 545.177 tokens-per-sec
Generation: 200 tokens, 106.805 tokens-per-sec
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
A transformer neural network is a type of deep learning model that is widely used for natural language processing (NLP) tasks such as language translation, text summarization, and sentiment analysis. Here's a step-by-step explanation of how a transformer processes a sentence:

1. Tokenization: The input sentence is first tokenized into individual words or subwords. This is done using a tokenizer, which is a pre-trained model that can convert text into a sequence of tokens.

2. Embedding: Each token is then converted into a dense vector representation using an embedding layer. The embedding layer is a pre-trained model that can convert tokens into a fixed-length vector representation.

3. Positional Encoding: The positional encoding layer is added to the input sequence to provide information about the position of each token in the sequence. This is important because transformers do not have an inherent understanding of the order of tokens in a sequence.

4. Self-Attention: The self-attention mechanism is used to compute the attention weights
==========
Prompt: 51 tokens, 95.358 tokens-per-sec
Generation: 200 tokens, 42.870 tokens-per-sec
Peak memory: 15.032 GB
```
</details>

### long_sequence — ran

<details><summary>stdout</summary>

```
==========
Certainly! Below is a simple implementation of a **Space Invaders** game using HTML and JavaScript. This version uses only HTML and JavaScript (no external libraries), and is designed for a single player. The game features:

- A player spaceship at the bottom of the screen.
- Invaders that move horizontally and shoot at the player.
- The player can move left and right.
- The player can shoot at invaders.
- Invaders are destroyed when hit by a bullet.
- The game ends when all invaders are destroyed or the player is hit.

---

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Space Invaders</title>
  <style>
    body { background: #000; color: #fff; font-family: sans-serif; }
    #game { position: absolute; top: 0; left: 0; width: 100vw; height: 100vh; overflow: hidden; }
    #game canvas { display: block; }
    #game #score { position: absolute; top: 10px; right: 10px; font-size: 24px; color: #fff; }
    #game #gameover { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 48px; color: #fff; }
    #game #gameover p { margin: 10px 0; }
  </style>
</head>
<body>
  <div id="game">
    <canvas id="canvas"></canvas>
    <div id="score">Score: 0</div>
    <div id="gameover"></div>
  </div>
  <script>
    // Game constants
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const width = canvas.width = window.innerWidth;
    const height = canvas.height = window.innerHeight;
    const playerSpeed = 5;
    const bulletSpeed = 10;
    const bulletWidth = 5;
    const bulletHeight = 15;
    const invaderSpeed = 1;
    const invaderDrop = 30;
    const invaderWidth = 40;
    const invaderHeight = 40;
    const playerWidth = 60;
    const playerHeight = 40;
    const playerX = width/2 - playerWidth/2;
    const playerY = height - playerHeight - 10;
    const playerXMin = 0;
    const playerXMax = width - playerWidth;
    const invaderXMin = 0;
    const invaderXMax = width - invaderWidth;
    const invaderY = 50;
    const invaderYMax = height - invaderHeight - 10;
    const invaderCount = 8;
    const invaderRows = 3;
    const invaders = [];
    let shooting = false;
    let shootingCooldown = 0;
    let score = 0;
    let gameover = false;

    // Player
    let player = {
      x: playerX,
      y: playerY,
      width: playerWidth,
      height: playerHeight,
      speed: playerSpeed,
      shootCooldown: 0,
      shootCooldownMax: 30,
      shootCooldownDec: 0.5,
      shootCooldownInc: 0.5,
      shootCooldownDecMax: 0.5,
      shootCooldownIncMax: 0.5,
      shootCooldownDecMin: 0.1,
      shootCooldownIncMin: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shootCooldownDecMinDec: 0.1,
      shootCooldownIncMinDec: 0.1,
      shootCooldownDecMaxInc: 0.5,
      shootCooldownIncMaxInc: 0.5,
      shootCooldownDecMinInc: 0.1,
      shootCooldownIncMinInc: 0.1,
      shootCooldownDecMaxDec: 0.5,
      shootCooldownIncMaxDec: 0.5,
      shoot
==========
Prompt: 49 tokens, 400.346 tokens-per-sec
Generation: 4096 tokens, 41.513 tokens-per-sec
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
MLX logits - min: -35.5000, max: 8.0625, mean: -17.6803, std: 4.6794

Absolute diff - min: 0.000000, max: 4.580130, mean: 0.516765
Relative diff - min: 0.000000, max: 866.771973, mean: 0.033249

Tolerance checks (% of values within threshold):
  < 0.001: 0.18%
  < 0.01: 1.77%
  < 0.1: 18.46%
  < 1.0: 83.82%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      617        ' have'              0.284796   617        ' have'              0.263736  
2      304        ' in'                0.192666   3073       ' exist'             0.207819  
3      3073       ' exist'             0.143044   527        ' are'               0.161219  
4      527        ' are'               0.068259   304        ' in'                0.103432  
5      11         ','                  0.057079   11         ','                  0.077884  
6      649        ' can'               0.025840   649        ' can'               0.024151  
7      1051       ' were'              0.024295   1101       ' also'              0.022162  
8      5101       ' appear'            0.017901   5101       ' appear'            0.014534  
9      449        ' with'              0.017404   477        ' or'                0.013977  
10     505        ' from'              0.016584   1051       ' were'              0.013131  

============================================================
OVERLAP ANALYSIS
============================================================

Top-1 match: True
  HF:  617 (' have')
  MLX: 617 (' have')

Top-5 overlap: 5/5
  HF:  [np.int64(617), np.int64(304), np.int64(3073), np.int64(527), np.int64(11)]
  MLX: [np.int64(617), np.int64(3073), np.int64(527), np.int64(304), np.int64(11)]

Top-10 overlap: 8/10

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
A transformer neural network is a type of deep learning model that is commonly used for natural language processing tasks such as language translation, text summarization, and sentiment analysis. Here is a step-by-step explanation of how a transformer processes a sentence:

1. Tokenization: The input sentence is first tokenized into individual words or subwords. This is done to break the sentence into smaller, more manageable pieces that can be processed by the model.

2. Embedding: Each token is then converted into a dense vector representation using an embedding layer. This vector representation captures the semantic meaning of the token and allows the model to understand the context in which it appears.

3. Positional Encoding: Positional encoding is added to the token embeddings to provide information about the position of each token in the sentence. This is important because the order of the tokens in a sentence is important for understanding the meaning.

4. Self-Attention: The self-attention mechanism is used to compute the attention weights between each token in
==========
Prompt: 51 tokens, 513.708 tokens-per-sec
Generation: 200 tokens, 104.562 tokens-per-sec
Peak memory: 4.424 GB
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

