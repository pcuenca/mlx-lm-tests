# Test Results: PR #1227

- **PR:** [ivanfioravanti/mlx-lm#1227](https://github.com/ivanfioravanti/mlx-lm/pull/1227)
- **Branch:** `add-ling-2.6-flash`
- **Commit:** [`4d4758dca32f03b66bf3224e5be030b61e4e9237`](https://github.com/ivanfioravanti/mlx-lm/commit/4d4758dca32f03b66bf3224e5be030b61e4e9237)
- **Model type:** `bailing_hybrid`
- **Timestamp:** 2026-05-14T16:49:36+00:00

## Numerical comparison (transformers vs MLX)

| Variant | Max diff | Mean diff | <0.01 | <0.1 | Top-1 | Top-5 | Top-10 |
|---|---|---|---|---|---|---|---|
| [`inclusionAI/Ling-2.6-flash`](#inclusionailing-26-flash) | 1.656250 | 0.125123 | 11.99% | 51.63% | True | 5/5 | 9/10 |

## Layer-by-layer comparison

| Variant | Worst layer | Diverged | Post-norm | Logits rel | Logits max diff |
|---|---|---|---|---|---|
| [`inclusionAI/Ling-2.6-flash`](#inclusionailing-26-flash) | layer 27 (3.52%) | 0 | 3.55% | 6.25% | 1.6562 |

## inclusionAI/Ling-2.6-flash

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
Here is a step-by-step explanation of how a **Transformer** neural network (specifically the "Encoder" part, like in BERT or the Decoder part like in GPT) processes a sentence.

For simplicity, we will use the example sentence: **"The cat sat."**

---

### Phase 1: Input Preparation
Before the math begins, the raw text must be converted into numbers.

**1. Tokenization**
The sentence is broken down into units the model understands (tokens).
*   "The" -> `101`
*   "cat" -> `1045`
*   "sat" -> `2665`
*   "." -> `1012`
*(These are placeholder IDs; actual models use large vocabularies).*

**2. Adding Embeddings**
Each token is converted into a high-dimensional vector (Embedding). This captures the meaning of
==========
Prompt: 32 tokens, 98.472 tokens-per-sec
Generation: 200 tokens, 40.103 tokens-per-sec
Peak memory: 214.816 GB
````
</details>

### layers — ran

<details><summary>stdout</summary>

````text
Model: inclusionAI/Ling-2.6-flash
Prompt: 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences'
trust_remote_code: True
reference_from: /Users/pedro/code/bailing_hybrid/mlx-lm-tests/work/pr-1227/4d4758d/references/inclusionAI--Ling-2.6-flash/numerical.safetensors
Token count: 81 (from reference)
Reference metadata: {'num_hidden_layers': '32', 'transformers_version': '4.56.2', 'model': 'inclusionAI/Ling-2.6-flash', 'compute_dtype': 'bfloat16', 'generated_at': '2026-05-14T16:45:41+00:00', 'prompt': 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences', 'torch_version': '2.12.0+cu130'}
Loading MLX model...

Collected 33 transformers states, 33 MLX states (transformers dtype=bfloat16, MLX dtype=bfloat16)

pos          max diff  mean diff    max |T|  max |MLX|   rel diff  status
-------------------------------------------------------------------------
layer 0        0.0156     0.0003       1.71       1.70     0.91%  ok
layer 1        0.0312     0.0008       3.23       3.23     0.97%  ok
layer 2        0.0713     0.0019       7.56       7.50     0.94%  ok
layer 3        0.1250     0.0036      13.69      13.69     0.91%  ok
layer 4        0.3750     0.0057      20.50      20.75     1.83%  warn
layer 5        1.0000     0.0079      94.00      94.00     1.06%  warn
layer 6        8.0000     0.0102    1304.00    1304.00     0.61%  ok
layer 7        8.0000     0.0138    1328.00    1328.00     0.60%  ok
layer 8        8.0000     0.0209    1328.00    1328.00     0.60%  ok
layer 9        8.0000     0.0281    1336.00    1336.00     0.60%  ok
layer 10       8.0000     0.0351    1336.00    1336.00     0.60%  ok
layer 11       8.0000     0.0466    1344.00    1344.00     0.60%  ok
layer 12       8.0000     0.0578    1344.00    1344.00     0.60%  ok
layer 13       8.0000     0.0672    1344.00    1344.00     0.60%  ok
layer 14       8.0000     0.0802    1408.00    1408.00     0.57%  ok
layer 15       8.0000     0.0968    1408.00    1408.00     0.57%  ok
layer 16       8.0000     0.1096    1408.00    1408.00     0.57%  ok
layer 17       8.0000     0.1253    1408.00    1408.00     0.57%  ok
layer 18       8.0000     0.1406    1408.00    1408.00     0.57%  ok
layer 19       8.0000     0.1578    1408.00    1408.00     0.57%  ok
layer 20       8.0000     0.1752    1416.00    1416.00     0.56%  ok
layer 21       8.0000     0.1993    1456.00    1456.00     0.55%  ok
layer 22       8.0000     0.2241    1552.00    1552.00     0.52%  ok
layer 23       9.0000     0.2472     500.00     500.00     1.80%  warn
layer 24      10.0000     0.2690     388.00     386.00     2.58%  warn
layer 25      12.0000     0.2921     440.00     438.00     2.73%  warn
layer 26      12.0000     0.3230     442.00     440.00     2.71%  warn
layer 27      16.0000     0.3586     454.00     450.00     3.52%  warn
layer 28      16.0000     0.3965     464.00     466.00     3.45%  warn
layer 29      20.0000     0.4332     720.00     724.00     2.78%  warn
layer 30      28.0000     0.4746    2272.00    2272.00     1.23%  warn
post-norm      2.4297     0.0558      68.50      68.50     3.55%  warn
logits         1.6562     0.1251      26.50      27.00     6.25%  warn

All layers within tolerance (<10% of signal magnitude).
````
</details>

### long_sequence — ran

<details><summary>stdout</summary>

````text
==========
Here's a **complete HTML and JavaScript implementation of a simplified version of Space Invaders**. This version includes:

- A player-controlled spaceship (left/right movement)
- Shooting bullets
- Falling alien invaders
- Basic collision detection
- Game over and win conditions

You can copy and paste this into a `.html` file and open it in your browser.

---

### ✅ Full Space Invaders Game (HTML + JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Space Invaders</title>
  <style>
    body {
      margin: 0;
      background: black;
      color: white;
      font-family: sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      overflow: hidden;
    }
    canvas {
      background: #000;
      border: 2px solid #fff;
    }
    #gameOver {
      display: none;
      font-size: 2em;
      color: red;
    }
  </style>
</head>
<body>
  <canvas id="gameCanvas" width="600" height="800"></canvas>
  <div id="gameOver">Game Over</div>
  <script>
    const canvas = document.getElementById("gameCanvas");
    const ctx = canvas.getContext("2d");

    const player = {
      x: canvas.width / 2 - 25,
      y: canvas.height - 60,
      width: 50,
      height: 30,
      speed: 5,
      color: "lime"
    };

    const bullets = [];
    const aliens = [];
    const alienBullets = [];

    let rightPressed = false;
    let leftPressed = false;
    let shootInterval = 0;
    let alienDirection = 1;
    let alienSpeed = 1;
    let alienDropAmount = 15;
    let alienMoveTimer = 0;
    let alienShootTimer = 0;
    let gameOver = false;
    let score = 0;

    const alienRows = 5;
    const alienCols = 10;
    const alienPadding = 30;

    // Initialize aliens
    function initAliens() {
      aliens.length = 0;
      for (let r = 0; r < alienRows; r++) {
        for (let c = 0; c < alienCols; c++) {
          aliens.push({
            x: c * alienPadding + 50,
            y: r * alienPadding + 50,
            width: 30,
            height: 20,
            alive: true
          });
        }
      }
    }

    // Draw player
    function drawPlayer() {
      ctx.fillStyle = player.color;
      ctx.fillRect(player.x, player.y, player.width, player.height);
    }

    // Draw bullets
    function drawBullets() {
      ctx.fillStyle = "white";
      for (let b of bullets) {
        ctx.fillRect(b.x, b.y, b.width, b.height);
      }
    }

    // Draw aliens
    function drawAliens() {
      for (let a of aliens) {
        if (!a.alive) continue;
        ctx.fillStyle = "red";
        ctx.fillRect(a.x, a.y, a.width, a.height);
      }
    }

    // Draw alien bullets
    function drawAlienBullets() {
      ctx.fillStyle = "yellow";
      for (let b of alienBullets) {
        ctx.fillRect(b.x, b.y, b.width, b.height);
      }
    }

    // Collision detection
    function rectCollide(a, b) {
      return (
        a.x < b.x + b.width &&
        a.x + a.width > b.x &&
        a.y < b.y + b.height &&
        a.y + a.height > b.y
      );
    }

    // Update game logic
    function update() {
      if (gameOver) return;

      // Player movement
      if (rightPressed && player.x + player.width < canvas.width) {
        player.x += player.speed;
      }
      if (leftPressed && player.x > 0) {
        player.x -= player.speed;
      }

      // Shooting
      shootInterval++;
      if (shootInterval % 10 === 0) {
        bullets.push({
          x: player.x + player.width / 2 - 2,
          y: player.y,
          width: 4,
          height: 10
        });
      }

      // Alien movement
      alienMoveTimer++;
      if (alienMoveTimer % 30 === 0) {
        let moveDown = false;
        for (let a of aliens) {
          if (!a.alive) continue;
          a.x += alienDirection * alienSpeed;
          if (a.x + a.width >= canvas.width || a.x <= 0) {
            moveDown = true;
          }
        }
        if (moveDown) {
          alienDirection *= -1;
          for (let a of aliens) {
            if (a.alive) a.y += alienDropAmount;
          }
        }
      }

      // Alien shooting
      alienShootTimer++;
      if (alienShootTimer % 60 === 0) {
        for (let a of aliens) {
          if (!a.alive) continue;
          alienBullets.push({
            x: a.x + a.width / 2 - 2,
            y: a.y + a.height,
            width: 4,
            height: 10
          });
        }
      }

      // Update bullets
      for (let i = bullets.length - 1; i >= 0; i--) {
        bullets[i].y -= 6;
        if (bullets[i].y < 0) {
          bullets.splice(i, 1);
        }
      }

      // Update alien bullets
      for (let i = alienBullets.length - 1; i >= 0; i--) {
        alienBullets[i].y += 4;
        if (alienBullets[i].y > canvas.height) {
          alienBullets.splice(i, 1);
        }
      }

      // Collision: bullet vs alien
      for (let i = bullets.length - 1; i >= 0; i--) {
        let hit = false;
        for (let a of aliens) {
          if (!a.alive) continue;
          if (rectCollide(bullets[i], a)) {
            a.alive = false;
            bullets.splice(i, 1);
            score += 10;
            hit = true;
            break;
          }
        }
        if (hit) break;
      }

      // Collision: alien bullet vs player
      for (let i = alienBullets.length - 1; i >= 0; i--) {
        if (rectCollide(alienBullets[i], player)) {
          gameOver = true;
          document.getElementById("gameOver").style.display = "block";
          return;
        }
      }

      // Check win condition
      let allDead = true;
      for (let a of aliens) {
        if (a.alive) {
          allDead = false;
          break;
        }
      }
      if (allDead) {
        gameOver = true;
        document.getElementById("gameOver").innerText = "You Win!";
        document.getElementById("gameOver").style.display = "block";
      }
    }

    // Render game
    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      drawPlayer();
      drawBullets();
      drawAliens();
      drawAlienBullets();
    }

    // Game loop
    function gameLoop() {
      update();
      render();
      if (!gameOver) {
        requestAnimationFrame(gameLoop);
      }
    }

    // Event listeners
    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight") rightPressed = true;
      if (e.key === "ArrowLeft") leftPressed = true;
      if (e.key === " " || e.key === "ArrowUp") {
        e.preventDefault();
        // Manual shoot
        bullets.push({
          x: player.x + player.width / 2 - 2,
          y: player.y,
          width: 4,
          height: 10
        });
      }
    });

    document.addEventListener("keyup", (e) => {
      if (e.key === "ArrowRight") rightPressed = false;
      if (e.key === "ArrowLeft") leftPressed = false;
    });

    // Start game
    initAliens();
    gameLoop();
  </script>
</body>
</html>
```

---

### 🕹️ Controls:

- **Left Arrow** / **A**: Move left
- **Right Arrow** / **D**: Move right
- **Space** / **Up Arrow**: Shoot

---

### 🧠 Features Implemented:

- Player movement and shooting
- Alien movement (side to side and down)
- Alien shooting
- Collision detection (bullets destroy aliens, alien bullets kill player)
- Win/lose conditions
- Score tracking

---

Let me know if you'd like to add:
- Sound effects
- Levels
- Power-ups
- More advanced alien behavior
- Mobile touch controls

Happy coding! 🚀
==========
Prompt: 31 tokens, 98.141 tokens-per-sec
Generation: 2300 tokens, 39.694 tokens-per-sec
Peak memory: 214.816 GB
````
</details>

### predictions — ran

<details><summary>stdout</summary>

````text
=== TRANSFORMERS vs MLX COMPARISON ===
Model: inclusionAI/Ling-2.6-flash
Prompt: 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences'
trust_remote_code: True
reference_from: /Users/pedro/code/bailing_hybrid/mlx-lm-tests/work/pr-1227/4d4758d/references/inclusionAI--Ling-2.6-flash/numerical.safetensors

Loaded reference: 81 tokens, logits shape (1, 81, 157184)
Reference metadata: {'model': 'inclusionAI/Ling-2.6-flash', 'generated_at': '2026-05-14T16:45:41+00:00', 'transformers_version': '4.56.2', 'torch_version': '2.12.0+cu130', 'prompt': 'The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet at least once and has been used as a typing exercise for over a century. In the world of computing, pangrams like this one serve a practical purpose beyond mere amusement. They help test fonts, keyboards, and text rendering systems by exercising the full range of characters that a system must support. Similar sentences', 'num_hidden_layers': '32', 'compute_dtype': 'bfloat16'}
Loading MLX model...

Tokens (HF):  [678, 3901, 13187, 46998, 40977, 997, 268, 27028, 7339, 13, 1077, 9606, 6543, 1380, 7885, 300, 268, 6212, 38574, 482, 3390, 3779, 301, 723, 1007, 1440, 409, 259, 28748, 8625, 352, 997, 259, 9685, 13, 718, 268, 1931, 300, 18359, 11, 282, 780, 46130, 1029, 501, 810, 7987, 259, 11012, 6189, 7267, 11616, 62911, 13, 2240, 1376, 1620, 42143, 11, 83419, 11, 301, 3019, 28613, 4519, 527, 43670, 268, 2771, 3278, 300, 7114, 378, 259, 1652, 2022, 1869, 13, 29340, 21356]
Tokens (MLX): [678, 3901, 13187, 46998, 40977, 997, 268, 27028, 7339, 13, 1077, 9606, 6543, 1380, 7885, 300, 268, 6212, 38574, 482, 3390, 3779, 301, 723, 1007, 1440, 409, 259, 28748, 8625, 352, 997, 259, 9685, 13, 718, 268, 1931, 300, 18359, 11, 282, 780, 46130, 1029, 501, 810, 7987, 259, 11012, 6189, 7267, 11616, 62911, 13, 2240, 1376, 1620, 42143, 11, 83419, 11, 301, 3019, 28613, 4519, 527, 43670, 268, 2771, 3278, 300, 7114, 378, 259, 1652, 2022, 1869, 13, 29340, 21356]

============================================================
NUMERICAL COMPARISON
============================================================

Shape - HF: (1, 81, 157184), MLX: (1, 81, 157184)

HF logits  - min: -23.3750, max: 26.5000, mean: -7.3875, std: 3.0635
MLX logits - min: -23.1250, max: 27.0000, mean: -7.3745, std: 3.0452

Absolute diff - min: 0.000000, max: 1.656250, mean: 0.125123
Relative diff - min: 0.000000, max: 55168.449219, mean: 0.055450

Tolerance checks (% of values within threshold):
  < 0.001: 11.76%
  < 0.01: 11.99%
  < 0.1: 51.63%
  < 1.0: 99.99%

============================================================
TOP 10 PREDICTIONS (last token)
============================================================

Rank   HF Token   HF Text              HF Prob    MLX Token  MLX Text             MLX Prob  
------------------------------------------------------------------------------------------------
1      3804       ' exist'             0.326928   3804       ' exist'             0.333560  
2      449        ' are'               0.211081   449        ' are'               0.215362  
3      561        ' have'              0.186278   561        ' have'              0.178542  
4      296        ' in'                0.099707   296        ' in'                0.115275  
5      11         ','                  0.060476   11         ','                  0.042407  
6      560        ' can'               0.022248   560        ' can'               0.022699  
7      911        ' also'              0.014364   911        ' also'              0.015601  
8      5397       ' appear'            0.005988   5397       ' appear'            0.008351  
9      453        ' or'                0.005284   453        ' or'                0.004758  
10     1275       '—'                  0.004964   378        ' that'              0.004470  

============================================================
OVERLAP ANALYSIS
============================================================

Top-1 match: True
  HF:  3804 (' exist')
  MLX: 3804 (' exist')

Top-5 overlap: 5/5
  HF:  [np.int64(3804), np.int64(449), np.int64(561), np.int64(296), np.int64(11)]
  MLX: [np.int64(3804), np.int64(449), np.int64(561), np.int64(296), np.int64(11)]

Top-10 overlap: 9/10

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
Here is a step-by-step breakdown of how a Transformer processes a sentence, from the raw text to the final output.

We will use the example of a standard "Encoder" stack (like the one used in BERT) processing the sentence:
**"The cat sat."**

---

### 1. Input Representation: Tokenization
The first step is to convert the sentence into a format the computer can understand.

*   **Tokenization:** The sentence is split into smaller units called **tokens**. This is usually done using a vocabulary list.
    *   `"The"` -> `101`
    *   `"cat"` -> `2023`
    *   `"sat"` -> `3032`
    *   `"."` -> `102`
*   **Special Tokens:** Special markers are added:
    *   `[CLS]` (Classification token) is added at the beginning
==========
Prompt: 32 tokens, 298.588 tokens-per-sec
Generation: 200 tokens, 74.786 tokens-per-sec
Peak memory: 58.709 GB
````
</details>

### quantize — ran

<details><summary>stdout</summary>

````text
[INFO] Loading
[INFO] Using dtype: bfloat16
[INFO] Quantizing
[INFO] Quantized model with 4.501 bits per weight.
````
</details>

## Notes

bailing_hybrid (BailingMoeV2_5) is not in transformers yet — the model loads only with trust_remote_code=True via the auto_map in config.json. Hybrid architecture: 1:7 ratio of MLA to Lightning-style linear attention (MLA at layers 7/15/23/31), plus sigmoid noaux_tc MoE (256 experts, 1 shared, group-limited top-8). Particular things to eyeball:
  - Layer-by-layer comparison: linear-attention layers can drift more than
    MLA layers; check whether divergence is concentrated at MLA boundaries.
  - sanitize() drops the trailing MTP layer and stacks MoE experts; if
    weight loading is off, expect catastrophic logits divergence.
  - rope_theta is 6e6 with partial_rotary_factor 0.5 — RoPE
    misconfiguration shows up after ~100 tokens.

