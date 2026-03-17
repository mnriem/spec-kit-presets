# spec-kit-presets

A personal collection of [spec-kit](https://github.com/github/spec-kit) presets by [@mnriem](https://github.com/mnriem).

A preset is a package of custom templates and agent commands that transforms how every spec-kit agent behaves — replacing the default output style, terminology, and structure without changing any tooling.

## Available Presets

| Preset | Description |
|--------|-------------|
| [pirate](./pirate/) | Transforms all spec-kit output into pirate speak — specs become "Voyage Manifests", plans become "Battle Plans", tasks become "Crew Assignments" |

## Installation

```bash
specify preset add --from https://github.com/mnriem/spec-kit-presets/releases/download/v1.0.0/<preset-name>.zip
```

Or from a local clone:

```bash
specify preset add --dev ./pirate
```

See each preset's README for specific installation and usage instructions.

## License

MIT
