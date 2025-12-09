from sympy import symbols, Eq, solve as sympy_solve

# רשימת היסודות
ELEMENTS = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'I', 'Te', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Uut', 'Uuq', 'Uup', 'Uuh', 'Uus', 'Uuo'
]

def generate_equation_for_element(compounds, coefficients, element):
    """Generates a symbolic equation for the given element."""
    equation = 0
    for i, compound in enumerate(compounds):
        if element in compound:
            equation += coefficients[i] * compound[element]
    return equation

def build_equations(reactant_atoms, product_atoms):
    """Builds a list of symbolic equations for each element."""
    ## coefficients ##
    reactant_coefficients = list(symbols(f'a0:{len(reactant_atoms)}'))
    product_coefficients = list(symbols(f'b0:{len(product_atoms)}')) 
    # אילוץ שהמקדם האחרון הוא 1, לכן פותרים עבור כל השאר
    product_coefficients = product_coefficients[:-1] + [1] 

    ## equations ##
    equations = []
    for element in ELEMENTS:
        lhs = generate_equation_for_element(reactant_atoms, reactant_coefficients, element)
        rhs = generate_equation_for_element(product_atoms, product_coefficients, element)
        if lhs != 0 or rhs != 0:
            equations.append(Eq(lhs, rhs))

    # מחזיר את רשימת המשוואות ואת רשימת המקדמים שיש לפתור (ללא המקדם 1)
    return equations, reactant_coefficients + product_coefficients[:-1]

def my_solve(equations, coefficients):
    """Solves the system of equations for the coefficients of the reaction."""
    solution = sympy_solve(equations, coefficients)

    if isinstance(solution, dict) and len(solution) == len(coefficients):
        coefficient_values = []
        for coefficient in coefficients:
            # המרה מפורשת ל-float כדי למנוע שגיאות דיוק בהשוואת הטסטים
            coefficient_values.append(float(solution[coefficient]))
        return coefficient_values

    return []
