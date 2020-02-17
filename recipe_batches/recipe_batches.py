#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = float("inf")
    for i, j in recipe.items():
        try:
            max_for_ingredient = ingredients[i] // j
        except KeyError:
            # if a required ingredient is missing, 0 batches can be made
            return 0
        # max batches limited to the least available ingredient
        max_batches = min(max_batches, max_for_ingredient)
    return max_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
