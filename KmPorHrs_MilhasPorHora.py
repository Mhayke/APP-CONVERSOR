def KMHrs_MilhasHrs():
    KmPorHora = int(input("Digite a quantidade de Km Por Horas para converter em milhas por hora:"))
    MilhasPorHora = float(KmPorHora * 1.609344)

    print(f"{KmPorHora} Km por hora é igual a {MilhasPorHora:.2f} milhas por hora.")

KMHrs_MilhasHrs()