# 🟠 encode-and-decode-tinyurl — Encode and Decode TinyURL

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/encode-and-decode-tinyurl/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Encode a long URL to a shortened URL and decode it back to the original URL.

## 🔍 Key Observation

The problem requires a simple mapping between long URLs and short URLs, which can be achieved using a dictionary.

## ⚙️ Algorithm

1. Use a dictionary to map each long URL to a unique short URL. This can be done by generating a unique key for each long URL and storing it in the dictionary with the long URL as the value.
2. When encoding a long URL, generate a unique key and store it in the dictionary.
3. When decoding a short URL, retrieve the corresponding long URL from the dictionary using the short URL as the key.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) for both encoding and decoding operations due to dictionary lookups.` | `O(n) where n is the number of URLs stored in the dictionary.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

</details>
