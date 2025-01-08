Overall, I think the logic is sound, however there are some things that stand out to me as red flags:

#### `exact_change` is defined, but never called from `main`

This automatically would fail the code review for me, as `exact_change` is dead code and shows a fundamental issue with the understanding of programming/testing concepts.

The logic is duplicated between `main` and `exact_change`, rather than `main` calling `exact_change`, so your effective test coverage is 0%.
This means I can change the logic in `main` all I want and still have every test pass, and that's a big issue, especially when working at a client.

#### Individual functions are doing too much

When creating functions, I try to follow the idea of the single responsibility principle (SRP).
This principle states that your code should do one thing and do it well. 
`exact_change` currently does many things (convert to cents, calculate the proper currencies, display it back to the user).
Break that function down into its individual actions and you'll be able to more easily see what is going on in a function. 

To draw and example of how I would break down your `main` method into functions
For example
```python
def main():    
    user_input = get_user_input()
    cents = convert_to_cents(user_input)
    minimum_cash = calculate_minimum_cash(cents)
    display_minimum_cash(minimum_cash)
```

#### The tests that do exist have too large of a scope to cover your edge cases
To go along with the previous point, when you break down your code into smaller functions you are able to test those functions at a more granular level.
This also allows you to test your edge cases more easily.

For example:
```python
def convert_to_cents():
    #logic to convert string to cents
    return

def test_convert_to_cents_should_round_when_more_than_two_decimal_places_given():
def test_convert_to_cents_should_expect_zero_cents_when_no_decimal_given():
# What happens when the user inputs an invalid value? Do we have incomplete code? Do we need validation?
```

You can hopefully see that those tests are fairly straightforward, but they should give you more confidence that the individual pieces of your code are working.
It's important to have tests that 

#### Function naming is somewhat ambiguous

When naming functions, I tend to try to make them start with a verb and be descriptive of the one action they do, like `calculate_minimum_cash`.

Without context clues, I would expect something named `exact_change` to be a `float` with the exact amount of change due back in a transaction.

#### File upload for initial commit

Learn to use git, it's an essential tool for being a software engineer.
GUI tools are fine, but learning the command line can be a huge boon to when things go sideways with your GUI tool (and they eventually will).