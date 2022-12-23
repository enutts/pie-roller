# pie-roller
CLI tool that uses  DSL to roll dice and perform actions based on results

## Example Usage
roll 6 D6s
```
roller -s "[6d6]" # 6 3 1 4 2
```

roll 6 D6s and return rolls greater than 3
```
roller -s "[6d6 ig3]" # 6 4
```
... maybe just split actions with semicolons 


Each group of `[]` is an action, actions take >=0 inputs and produce outputs

every nested action takes the results of the higher nest as an output, solves actions left to right

ex using outputs from above (a adds all inputs)
```
roller -s "[6d6 ig3 ][a]" # 10
```