"""
    ``Autor``: Marlon Rogério
    ``AUTÔMATO DE PILA``
    ``Considerar``:
        {w ∈ {0,1}* | o número de zeros é igual o numero de uns }
    
    ``Alfabetos``:
        Σ = {0,1}; 
        Γ = {Z,F,U,λ} 

    Autômato para reconhecer expressão matemática
    ``Estados``: {igual, diferente}
    ``Regras`` (R): 
        igual <- 0 -> diff & Γ <- λ/F
        igual <- 1 -> diff & Γ <- λ/U
        diff <- 0 -> igual & Γ <- F/λ
        diff <- 1 -> igual & Γ <- U/λ
"""
E = ['igual', 'diferente']
Γ = [] #λ
i = E[0] #igual
F = E[0] #igual
e_atual = i

exp = input('Informe uma palavra para o alfabeto {0,1}*: ')

for t in exp:
    
    if e_atual == E[0] and t == '0': 
        e_atual = E[1]
        if not Γ:
            Γ = ['F']
        else:
            Γ.append('F')
    
    elif e_atual == E[0] and t == '1':
        e_atual = E[1]
        if not Γ:
            Γ = ['U']
        else:
            Γ.append('U')
    
    elif e_atual == E[1] and t == '0':
        e_atual = E[0]
        if 'U' in Γ:
            Γ.remove('U')
        if 'F' in Γ:
            Γ.remove('F')
    
    elif e_atual == E[1] and t == '1':
        e_atual = E[0]
        if 'F' in Γ:
            Γ.remove('F')
        if 'U' in Γ:
            Γ.remove('U')

if e_atual == F and not Γ:
    print('A paravra %s é reconhecida pelo autômoto' % exp)
else:
    print('A paravra %s não é reconhecida pelo autômoto' % exp)