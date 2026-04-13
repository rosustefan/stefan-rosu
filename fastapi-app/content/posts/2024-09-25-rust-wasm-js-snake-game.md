---
layout: post
title: Create the Snake Game in Rust/WebAssembly and Javascript
description: A Fun Way to Dive Deeper into Rust and WASM
tags: rust wasm js ts
categories: self-taught-programmer
---

Hello! Hope you're having a great day, and if not, let's make it a bit better! I recently completed a fantastic Udemy course by Filip JERGA: [Rust & WebAssembly with JS (TS) - The Practical Guide](https://www.udemy.com/course/rust-webassembly-with-js-ts-the-practical-guide/learn/lecture/29735156#overview), and I highly recommend it. If you want to dive deep into the beauty of Rust and experience the lightning-fast performance that WASM brings to web apps, this is for you!

In short, Rust lets you write performance-critical logic, compile it to WebAssembly (WASM), and then run it in the browser with JavaScript or TypeScript. This gives a significant speed boost compared to the just-in-time compiling used in native JS/TS.

I decided to take this course because Rust is an amazing language, but has a steep learning curve. Unlike Python, where you can reach a beginner level within six months, Rust takes more time to master. Although I’ve been through `The Book` and other entry-level courses, Filip's course stood out. It combines Rust, WASM, and JS/TS into one fun project: building a Snake game!

For all you old Nokia fans, you can play the Snake game I built [here](https://stefanrosu.ro/snake/). Have fun!

And here's a little Rust snippet for your enjoyment:

{% highlight rust linenos %}

#[wasm_bindgen]
impl World {
    pub fn new(width: usize, snake_idx: usize) -> World {
        let snake = Snake::new(snake_idx, 3);
        let size = width * width;

        World {
            width,
            size,
            reward_cell: World::gen_reward_cell(size, &snake.body),
            snake,
            next_cell: None,
            status: None,
            points: 0,
        }
    }
        
{% endhighlight %}