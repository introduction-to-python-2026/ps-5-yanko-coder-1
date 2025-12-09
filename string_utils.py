def split_before_each_uppercases(formula):
  start, end = 0,0
  split_formula = []
  for i,value in enumerate(formula):
    if i == 0:
     continue
    if value.isupper():
      end = i
      split_formula.append(formula[start:end])
      start = end
      if i == len(formula)-1:
         split_formula.append(formula[-1])
    elif i == len(formula)-1:
       split_formula.append(formula[start:])
  return split_formula


def split_at_digit(formula):
  for i,value in enumerate(formula):
     x = value.isdigit()
     if x:
        break
  if x:
     letters = formula[:i]
     digits = int(formula[i:])
  else:
     letters = formula
     digits = 1
  return letters, digits


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    # Split formula into segments at each uppercase letter
    segments = split_before_each_uppercases(molecular_formula)

    for seg in segments:
        # Extract the atom and its count (default 1)
        atom, count = split_at_digit(seg)

        # Step 2: Update the dictionary with the atom name and count
        atom_counts[atom] = atom_counts.get(atom, 0) + count

    # Step 3: Return the completed dictionary
    return atom_counts

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.
    Example: 'H2 + O2 -> H2O' -> (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries."""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
