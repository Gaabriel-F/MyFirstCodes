LarguraParede = float(input('Digite a largura da parede (m): '))
AlturaParede = float(input('Digite a altura da parede (m): '))

Metros2 = LarguraParede * AlturaParede

LitrosTinta = Metros2 / 2

print(f'Sua Parede tem a dimensão de {LarguraParede:.1f}x{LarguraParede:.1f} e sua área é de {Metros2}m²\nVocê precisará de {LitrosTinta:.2f}l de tinta')