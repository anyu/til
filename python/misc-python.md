# Misc Python

```python
>>> help(KEYWORD)
```

## Python project structure

- [sample simple repo](https://github.com/navdeep-G/samplemod)
- https://docs.python-guide.org/writing/structure/#

## Dependencies
- Use virtual environments to isolate dependencies between projects:
  ```sh
  # creates virtual env
  python3 -m venv venv

  # activate env
  source venv/bin/activate

  # deactivate env
  deactive
  ```

- Freeze deps: `pip freeze > requirements.txt`
- Install deps: `pip install -r requirements.txt`

## PyCharm

- Debugging via PyCharm: https://www.youtube.com/watch?v=QJtWxm12Eo0

## *args and **kwargs

#### `*args`
- The `*` is the key (technically `args` could be named whatever)
- Packs all arguments into a tuple
	```python
	def create_meeting(sub, *args):
		print(args)

	create_meeting("project planning", 2021, 10, 20)
	create_meeting("project planning", 2021, 10, 20, 14, 0)

	# (2021, 10, 20)
	# (2021, 10, 20, 14, 0)
	```

#### `**kwargs`
- The `**` is key (`kwargs` could be whatever)
- Packs arguments with keywords into a dictionary
	```python
	def draw_circle(radius, **kwargs):
		fill = "red"
		stroke = "yellow"
		if "fill" in kwargs:
			fill = kwargs["fill"]
		if "stroke" in kwargs:
			fill = kwargs["stroke"]
		print(f"Circle with radius {radius}, fill {fill}, stroke {stroke}")

	draw_circle(10, stroke="green")

	# Circle with radius 10, fill red, stroke green
	```
