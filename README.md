# spec-kit-presets

> **⚠️ Experimental** — This is the `mnriem` persona Spec Kit presets
> repository. The presets here are experimental and may change or break
> without notice.

This repository contains experimental
[Spec Kit](https://github.com/github/spec-kit) presets developed by
`mnriem`. These are personal experiments and are not official or
community-contributed presets.

A preset is a package of custom templates and agent commands that transforms
how every spec-kit agent behaves — replacing the default output style,
terminology, and structure without changing any tooling.

## Available Presets

| Preset | Description |
|--------|-------------|
| [aide-in-place](./aide-in-place/) | Adapts the AIDE extension workflow for in-place technology migrations (X → Y pattern) — adds migration objectives, verification gates, knowledge documents, and behavioral equivalence criteria |
| [pirate](./pirate/) | Transforms all spec-kit output into pirate speak — specs become "Voyage Manifests", plans become "Battle Plans", tasks become "Crew Assignments" |

## Forking

If you like a specific preset or all the presets in this repository, it is
recommended to **fork** this repository. This gives you a stable copy that
won't be affected by experimental changes made here.

## Usage

Add this catalog URL to your Spec Kit configuration:

```
https://raw.githubusercontent.com/mnriem/spec-kit-presets/main/catalog.json
```

Then install a preset with the Spec Kit CLI:

```bash
specify preset add --from https://github.com/mnriem/spec-kit-presets/releases/download/<preset>-v<version>/<preset>.zip
```

Or from a local clone:

```bash
specify preset add --dev ./<preset>
```

You can also browse individual presets by navigating to their directory
(e.g., [pirate/](pirate/)) and reading the README for more details.

## More Information

See the [Spec Kit README](https://github.com/github/spec-kit/blob/main/README.md)
for more information about Spec Kit and its preset system.

## License

MIT
