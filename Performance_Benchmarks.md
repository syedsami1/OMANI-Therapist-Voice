# ⏱ Performance Benchmarks

This file documents system latency and component-wise performance.

---

## 🎯 Goal: < 20s per conversation turn

### Component Breakdown (Tested on GPU - A100 / RTX 4090)

| Component       | Avg Time     |
|----------------|--------------|
| Google STT     | 1.5 – 2.0 s  |
| GPT-J Response | 10 – 12 s    |
| Google TTS     | 2 – 3 s      |
| Flask + I/O    | 1 – 2 s      |

**Total per-turn latency: ~16 – 18 seconds**

---

## 🧪 Observations

- Local inference greatly reduces costs.
- Faster results when batching multiple TTS requests.
- Google APIs are stable, responsive within free quota limits.
