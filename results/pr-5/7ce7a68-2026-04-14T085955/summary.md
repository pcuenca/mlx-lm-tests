# Test Results: PR #5

- **PR:** [pcuenca/mlx-lm#5](https://github.com/pcuenca/mlx-lm/pull/5)
- **Branch:** `olmo-hybrid-v2`
- **Commit:** [`7ce7a68789b7b0e5dbfb0b8d27f3f3d4b991d4a1`](https://github.com/pcuenca/mlx-lm/commit/7ce7a68789b7b0e5dbfb0b8d27f3f3d4b991d4a1)
- **Model type:** `olmo_hybrid`
- **Timestamp:** 2026-04-14T07:04:14+00:00

## Numerical comparison (transformers vs MLX)

| Variant | Max diff | Mean diff | <0.01 | <0.1 | Top-1 | Top-5 | Top-10 |
|---|---|---|---|---|---|---|---|
| `allenai/Olmo-Hybrid-7B` | 0.506462 | 0.073131 | 8.75% | 73.77% | True | 5/5 | 10/10 |
| `allenai/Olmo-Hybrid-Instruct-SFT-7B` | 0.255213 | 0.048441 | 12.98% | 90.18% | True | 5/5 | 10/10 |

## allenai/Olmo-Hybrid-7B

### dtype — PASS

<details><summary>stdout</summary>

````text
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
````
</details>

### generate — ran

<details><summary>stdout</summary>

````text
==========
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that were previously inaccessible to us.

One of the most exciting applications of gravitational wave astronomy is the study of the early universe, specifically the epoch known as the "Big Bang." This is the moment in time when the universe began, and it is believed to have occurred approximately 13.8 billion years ago. During this time, the universe was incredibly hot and dense, and it underwent a rapid expansion known as inflation. This inflationary period is thought to have lasted for a fraction of a second, but it had a profound impact on the structure and evolution of the universe.

One of the key predictions of inflationary theory is the existence of primordial gravitational waves. These are ripples in the fabric of spacetime that were generated during the inflationary period and have left an imprint on the cosmic microwave background radiation (CMB). The CMB is the afterglow of the Big Bang, and it provides us with
==========
Prompt: 57 tokens, 455.667 tokens-per-sec
Generation: 200 tokens, 43.022 tokens-per-sec
Peak memory: 15.042 GB
````
</details>

### long_sequence — ran

<details><summary>stdout</summary>

````text
==========
The tutorial should be divided into 5 Sections, each marked with Section N, and each section should contain at least 3 paragraphs. Repeat your response in Spanish language as well.

**Section 1: Introduction to Web Servers**

A web server is a software application that processes requests made over the internet. It receives requests from clients, processes them, and sends back responses. The most common protocol used for web servers is HTTP (Hypertext Transfer Protocol). Understanding the basics of how web servers work is crucial for anyone looking to develop web applications.

Web servers operate by listening on a specific port for incoming requests. When a request is received, the server processes it and sends back a response. This response can be a simple acknowledgment or a full HTML page. The server uses a combination of software and hardware to handle these requests efficiently.

Understanding the basics of web servers is essential for anyone looking to develop web applications. It involves understanding how requests are processed, how data is sent and received, and how to handle errors effectively. This foundational knowledge is crucial for anyone looking to develop web applications.

**Section 2: Setting Up the Environment**

Before diving into the development of a web server, it's important to set up the development environment. This involves installing the necessary software and configuring the system to ensure smooth development.

First, ensure that Python is installed on your system. Python is a versatile language that is widely used for web development. Once Python is installed, you can use it to write and run your web server code.

Next, you will need to install additional libraries that will help in handling HTTP requests and responses. Libraries such as `http.server` and `http.client` are essential for handling HTTP requests and responses in Python.

**Section 3: Implementing HTTP Requests**

Implementing HTTP requests involves understanding the structure of HTTP requests and responses. HTTP requests consist of a method (GET, POST, etc.), a URL, and optional headers. The server must parse these requests and generate appropriate responses.

To implement HTTP requests, you need to parse the request data, extract the method, URL, and headers, and then generate an appropriate response. This involves parsing the request data, extracting the necessary information, and generating a response based on the request.

**Section 4: Handling Requests and Responses**

Handling requests and responses involves parsing the incoming data, extracting relevant information, and generating appropriate responses. This involves parsing the request data, extracting relevant information, and generating appropriate responses based on the request.

Handling requests and responses involves parsing the incoming data, extracting relevant information, and generating appropriate responses based on the request. This involves parsing the request data, extracting relevant information, and generating appropriate responses based on the request.

**Section 5: Error Handling and Logging**

Error handling and logging are crucial components of any web server. They help in identifying and diagnosing issues that may arise during the operation of the server. Implementing robust error handling ensures that the server can handle unexpected errors gracefully and provide meaningful feedback to the user.

Error handling involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This includes handling errors such as invalid requests, server errors, and other unexpected issues. Effective error handling ensures that the server can handle unexpected issues gracefully and provide meaningful feedback to the user.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This includes handling errors such as invalid requests, server errors, and other unexpected issues.

Effective error handling ensures that the server can handle unexpected issues gracefully and provide meaningful feedback to the user. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests.

**Section 5: Error Handling**

Error handling is a critical aspect of web server development. It involves implementing mechanisms to catch and handle exceptions that may occur during the processing of requests. This involves implementing mechanisms to
==========
Prompt: 26 tokens, 227.504 tokens-per-sec
Generation: 4096 tokens, 41.960 tokens-per-sec
Peak memory: 15.525 GB
````
</details>

### predictions — ran

<details><summary>stdout</summary>

````text
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
MLX logits - min: -37.2500, max: 13.2500, mean: -14.9384, std: 5.8864

Absolute diff - min: 0.000000, max: 0.506462, mean: 0.073131
Relative diff - min: 0.000000, max: 1603.127197, mean: 0.009329

Tolerance checks (% of values within threshold):
  < 0.001: 0.88%
  < 0.01: 8.75%
  < 0.1: 73.77%
  < 1.0: 100.00%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      3073       ' exist'             0.214905   3073       ' exist'             0.202404  
2      617        ' have'              0.190557   617        ' have'              0.196177  
3      649        ' can'               0.169736   649        ' can'               0.162637  
4      527        ' are'               0.087119   527        ' are'               0.092667  
5      11         ','                  0.078129   11         ','                  0.081779  
6      304        ' in'                0.045007   304        ' in'                0.046596  
7      1101       ' also'              0.036058   1101       ' also'              0.037441  
8      2663       ' called'            0.012976   2663       ' called'            0.013774  
9      5101       ' appear'            0.011175   5101       ' appear'            0.011599  
10     477        ' or'                0.009946   477        ' or'                0.010236  

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
````
</details>

### quant_dtype — PASS

<details><summary>stdout</summary>

````text
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
````
</details>

### quant_generate — ran

<details><summary>stdout</summary>

````text
==========
gravitational waves provide a unique window into the early universe, allowing us to study phenomena that were previously inaccessible to us.

One of the most exciting applications of gravitational wave astronomy is the study of the early universe, specifically the epoch known as the "cosmic dawn." This period marks the transition from the dark ages of the universe, when it was filled with neutral hydrogen gas, to the era of star formation and galaxy evolution. During this time, the first stars and galaxies formed, and their light began to illuminate the cosmos. However, the process of star formation is complex and poorly understood, and the details of how it occurred remain shrouded in mystery.

One of the key challenges in studying the early universe is the fact that the universe was opaque during this time, making it difficult to observe directly. However, gravitational waves offer a unique window into this era, as they can penetrate the opaque universe and provide a direct view of the early cosmos. By studying the gravitational waves emitted during the early universe,
==========
Prompt: 57 tokens, 566.432 tokens-per-sec
Generation: 200 tokens, 105.754 tokens-per-sec
Peak memory: 4.442 GB
````
</details>

### quantize — ran

<details><summary>stdout</summary>

````text
[INFO] Loading
[INFO] Quantizing
[INFO] Quantized model with 4.502 bits per weight.
````
</details>

## allenai/Olmo-Hybrid-Instruct-SFT-7B

### dtype — PASS

<details><summary>stdout</summary>

````text
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
````
</details>

### generate — ran

<details><summary>stdout</summary>

````text
==========
A transformer neural network processes a sentence by encoding the input sequence into a sequence of vectors, then encoding those vectors into a context vector, and finally decoding the context vector into an output sequence. The transformer uses self-attention mechanisms to weigh the importance of different words in the input sequence, and it uses an encoder-decoder architecture to process the input sequence and generate the output sequence.
==========
Prompt: 51 tokens, 411.547 tokens-per-sec
Generation: 77 tokens, 43.196 tokens-per-sec
Peak memory: 15.033 GB
````
</details>

### long_sequence — ran

<details><summary>stdout</summary>

````text
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
    x: 100,
    y: 50,
    width: 50,
    height: 50,
    speed: 5
};

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPlayer();
    drawAlien();
}

function drawPlayer() {
    ctx.fillStyle = 'blue';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawAlien() {
    ctx.fillStyle = 'red';
    ctx.fillRect(alien.x, alien.y, alien.width, alien.height);
}

setInterval(draw, 1000);

// Move player
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowLeft' && player.x > 0) {
        player.x -= player.speed;
    }
    if (event.key === 'ArrowRight' && player.x < canvas.width - player.width) {
        player.x += player.speed;
    }
});
```

This is a very basic implementation of the game. It only includes the player and the alien, and the player can move left and right. The game logic, such as the alien moving, shooting, and the game over condition, are not included. You would need to add these to make the game more complete.
==========
Prompt: 49 tokens, 396.075 tokens-per-sec
Generation: 518 tokens, 42.616 tokens-per-sec
Peak memory: 15.033 GB
````
</details>

### predictions — ran

<details><summary>stdout</summary>

````text
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
MLX logits - min: -35.7500, max: 7.7812, mean: -17.2809, std: 4.6913

Absolute diff - min: 0.000000, max: 0.255213, mean: 0.048441
Relative diff - min: 0.000000, max: 50.214516, mean: 0.003100

Tolerance checks (% of values within threshold):
  < 0.001: 1.31%
  < 0.01: 12.98%
  < 0.1: 90.18%
  < 1.0: 100.00%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      617        ' have'              0.284796   617        ' have'              0.281233  
2      304        ' in'                0.192666   304        ' in'                0.187342  
3      3073       ' exist'             0.143044   3073       ' exist'             0.144202  
4      527        ' are'               0.068259   527        ' are'               0.070691  
5      11         ','                  0.057079   11         ','                  0.057052  
6      649        ' can'               0.025840   649        ' can'               0.026884  
7      1051       ' were'              0.024295   1051       ' were'              0.025453  
8      5101       ' appear'            0.017901   5101       ' appear'            0.018262  
9      449        ' with'              0.017404   449        ' with'              0.017290  
10     505        ' from'              0.016584   505        ' from'              0.015866  

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
````
</details>

### quant_dtype — PASS

<details><summary>stdout</summary>

````text
{
  "output_dtype": "mlx.core.bfloat16",
  "expected_dtype": "mlx.core.bfloat16",
  "match": true
}
````
</details>

### quant_generate — ran

<details><summary>stdout</summary>

````text
==========
A transformer neural network processes a sentence by encoding the input sequence into a fixed-length vector representation using self-attention mechanisms. The input sentence is first tokenized into individual words or subwords, and each token is represented as a vector. The transformer then processes the input sequence through multiple layers of self-attention, where each token is compared with every other token in the sequence to determine its importance relative to the others. The self-attention mechanism allows the model to capture long-range dependencies and relationships between words in the sentence. The output of the transformer is a fixed-length vector representation of the input sentence, which can be used for various natural language processing tasks such as sentiment analysis, question answering, and machine translation.
==========
Prompt: 51 tokens, 514.463 tokens-per-sec
Generation: 143 tokens, 105.306 tokens-per-sec
Peak memory: 4.427 GB
````
</details>

### quantize — ran

<details><summary>stdout</summary>

````text
[INFO] Loading
[INFO] Quantizing
[INFO] Quantized model with 4.502 bits per weight.
````
</details>

## Notes

DPO variant uses NoPE (rope_theta: null) while base/SFT/Think-SFT use RoPE with theta=10000. The numerical comparison at 100+ tokens should catch any RoPE misconfiguration across variants.

