# 🖼️ AI Image Generator

Generate high-resolution images from natural language prompts using **Nebius AI Studio** and the `black-forest-labs/flux-dev` model. This project demonstrates seamless integration of OpenAI-compatible APIs into a modern frontend architecture.

---

## 🚀 Features

- Text-to-image generation using Nebius AI
- Outputs 1024x1024 high-quality PNG images
- Prompt-based control with customizable parameters
- Built with Next.js (App Router) and Tailwind CSS
- Fully typed codebase with TypeScript

---

## 🧠 Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| AI Backend    | Nebius AI Studio (OpenAI API) |
| Image Model   | `black-forest-labs/flux-dev`  |
| Frontend      | Next.js (App Router)          |
| Styling       | Tailwind CSS                  |
| Language      | TypeScript                    |
| API Route     | Server Functions (Edge-ready) |

---

## 📦 Folder Structure

```
ai-image-generator/
├── app/
│   ├── page.tsx                ← Main UI page
│   └── api/generate/route.ts   ← API route to generate images
├── public/                     ← Static assets
├── styles/                     ← Tailwind/global CSS
├── tailwind.config.ts          ← Tailwind config
├── tsconfig.json               ← TypeScript config
└── ...
```

---

## 🧪 How It Works

1. User enters a text prompt.
2. The `POST /api/generate` route sends the prompt to Nebius AI via the OpenAI-compatible client.
3. Nebius processes the prompt using the `flux-dev` image model.
4. The server returns a generated image URL.
5. The image is rendered in the frontend.

> This approach ensures separation of concerns between UI and AI logic.

---

## 📥 Setup

```bash
# 1. Clone the project
git clone https://github.com/nageshkumarmishra/my-dev-portfolio.git
cd my-dev-portfolio/ai/ai-image-generator

# 2. Install dependencies
npm install

# 3. Create a .env.local file
echo "NEBUIS_API_KEY=your-nebius-api-key" > .env.local

# 4. Run locally
npm run dev
```

---

## 🔐 Environment Variables

| Variable         | Purpose                         |
|------------------|---------------------------------|
| `NEBUIS_API_KEY` | Your Nebius AI Studio API key   |

---

## 🧬 Model Parameters Used

```json
{
  "model": "black-forest-labs/flux-dev",
  "response_extension": "png",
  "width": 1024,
  "height": 1024,
  "num_inference_steps": 28,
  "negative_prompt": "",
  "seed": -1
}
```

---

## 🙋 About the Developer

**Nagesh Kumar Mishra**  
🔗 [LinkedIn](https://linkedin.com/in/nageshkumarmishra)  
🐙 [GitHub](https://github.com/nageshkumarmishra)

> This project is part of my [Developer Portfolio](https://github.com/nageshkumarmishra/my-dev-portfolio)

---

## 📜 License

MIT – free to use, modify, and share.