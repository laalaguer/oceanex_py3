# Important

Before test, put your `key.pem` inside this directory.

Before test, create a file `configuration.py` inside this directory.

And fill in the `configuration.py` with:

```
test_config = {
    'uid': 'xxxx',
    'apikey_id': 'xxxx',
    'private_key_location': '/xxx/xxx/xxx/key.pem'
}
```

# How to test

Just run `pytest`
