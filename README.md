# NEXORA

**Small, clear tools for everyday Python work.**

NEXORA is an open-source, cross-platform Python toolkit. Its first release focuses on
predictable text, file, system and network utilities, with no runtime dependencies.

## Install locally

```bash
python -m pip install -e .
```

## Quick start

```python
import nexora as nx

print(nx.text.clean("  Bonjour   Python !  "))
print(nx.text.word_count("Python rend le travail plus simple."))
print(nx.system.platform())
print(nx.network.is_online())
```

## Design principles

- Simple APIs with sensible defaults.
- No runtime dependencies in the core package.
- Clear exceptions rather than silent failures.
- Cross-platform behavior where possible.
- Tests and documentation for every public feature.

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

## License

MIT. See `LICENSE`.
