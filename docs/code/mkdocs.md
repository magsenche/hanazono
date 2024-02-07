# Mkdocs

## Plugins

1. Define the entry-poiint
```toml title="pyproject.toml"
[project.entry-points."mkdocs.plugins"]
custom_server = "plugin.custom_server:CustomServer"
```

2. Enable plugin
```yaml title="mkdocs.yml"
plugins:
- custom_server
```

3. Overwrite an [event](https://www.mkdocs.org/dev-guide/plugins/#events)
```python
class CustomServer(BasePlugin):
    def on_serve(self, server, config, builder):
        server._serve_request = get_custom_serve_request(server, config)
        return server
```

## Ressources

- official [dev guide](https://www.mkdocs.org/dev-guide/plugins/)

## Flashcards