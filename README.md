# mapreduce-starter
Starter code for "mutual-friend finding" using (simulated) MapReduce in python. Look at the `solution` branch for a complete implementation.

## The problem

Given some friend lists:
```
Alice -> Bob Carol Dan
Bob -> Alice Carol Dan Eve
Carol -> Alice Bob Dan Eve
Dan -> Alice Bob Carol Eve
Eve -> Bob Carol Dan
```

Find the mutual friends of each pair of people:
```
Alice, Bob -> Carol Dan
Alice, Carol -> Bob Dan
Alice, Dan -> Bob Carol
Bob, Carol -> Alice Dan Eve
Bob, Dan -> Alice Carol Eve
Bob, Eve -> Carol Dan
Carol, Dan -> Alice Bob Eve
Carol, Eve -> Bob Dan
Dan, Eve -> Bob Carol
```

### The setup

- Clone this repo. 
- Edit the `mapper` function in `mapper.py` and the `reducer` function in `reducer.py`. 
- Everything else, including input parsing and the shuffle step, is already implemented.
- Test your code with `python run.py`. This command prints only the final results. 
- Use `python debug.py` instead to see the input/output at each step.
