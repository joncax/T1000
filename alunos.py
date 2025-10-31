def get_student_data():
    """
    Collects student name and grades for disciplines pre-defined by the study year (5th to 9th).
    Uses a while loop to ensure valid year selection and valid grade input.
    """
    # Mapeamento das disciplinas por ano de estudo
    DISCIPLINAS_POR_ANO = {
        '5': [
            'Português', 'Inglês', 'História e Geografia de Portugal', 'Matemática', 
            'Ciências Naturais', 'Educação Visual', 'Educação Tecnológica', 'Educação Musical'
        ],
        '6': [
            'Português', 'Inglês', 'História e Geografia de Portugal', 'Matemática', 
            'Ciências Naturais', 'Educação Visual', 'Educação Tecnológica', 'Educação Musical'
        ],
        '7': [
            'Português', 'Matemática', 'Ciências Naturais', 'Inglês', 'Francês', 
            'Cidadania e Desenvolvimento', 'História e Geografia de Portugal', 'Artes Visuais', 
            'Educação Musical', 'Físico-Química'
        ],
        '8': [
            'Português', 'Matemática', 'Ciências Naturais', 'Inglês', 'Francês', 
            'Cidadania e Desenvolvimento', 'História e Geografia de Portugal', 'Artes Visuais', 
            'Educação Musical', 'Físico-Química'
        ],
        '9': [
            'Português', 'Matemática', 'Ciências Naturais', 'Inglês', 'Francês', 
            'Cidadania e Desenvolvimento', 'História e Geografia de Portugal', 'Artes Visuais', 
            'Educação Musical', 'Físico-Química'
        ]
    }

    name = input("Enter the student's name: ")
    
    # LOOP E DECISÃO: Garante que o ano seja válido (5 a 9)
    valid_year = False
    while not valid_year:
        year_input = input("Enter the student's study year (5 to 9): ").strip()
        if year_input in DISCIPLINAS_POR_ANO:
            study_year = year_input + "º Ano"
            disciplines = DISCIPLINAS_POR_ANO[year_input]
            valid_year = True
        else:
            # Controle de loop sem 'break'
            print("Invalid year. Please enter a year between 5 and 9.") 

    grades_data = [] # Lista para armazenar (grade, class_name)
    
    print(f"\n--- Entering grades for {study_year} ({len(disciplines)} classes) ---")

    # ESTRUTURA DE REPETIÇÃO (LOOP) para coletar as notas
    for discipline in disciplines:
        collecting_grade = True
        while collecting_grade: # Loop interno para garantir nota válida
            grade_input = input(f"Enter the grade for **{discipline}** (0-20): ").strip()
            
            try:
                grade = float(grade_input)
                # DECISÃO: Validação da nota
                if 0 <= grade <= 20:
                    grades_data.append((grade, discipline)) 
                    collecting_grade = False
                else:
                    print("Grade must be between 0 and 20. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numerical grade.")

    return name, study_year, grades_data


def calculate_average(grades_data_list):
    """
    Calculates the simple arithmetic average from the list of (grade, class_name) tuples.
    """
    # Extrai apenas as notas
    grades_only = [item[0] for item in grades_data_list]

    # DECISÃO: Evita divisão por zero
    if len(grades_only) == 0:
        return 0
    else:
        total_sum = sum(grades_only)
        count = len(grades_only)
        # Média Aritmética Simples
        average = total_sum / count
        return average


def display_results(name, year, grades_data, average):
    """
    Prints the collected and calculated data in the requested organized format.
    """
    separator = "=" * 40
    
    print("\n" + separator)
    print("Calculo da média das disciplinas")
    print(separator)

    # Exibição do Nome e Ano
    print(f"Nome do Aluno(a): {name}")
    print(f"Ano do Aluno(a): {year}\n")

    print(f"Classes:")

    # Loop para exibir disciplinas e notas com alinhamento
    if grades_data:
        for grade, class_name in grades_data:
            # Utiliza f-string padding para alinhamento
            print(f"\t- {class_name:<35} | {grade:>4.1f}") 
    else:
        print("\t- Nenhuma nota de disciplina inserida.")

    # Formato da Média
    formatted_average = f"{average:.2f}"

    # Saída Final
    print("\n" + separator)
    print(f"Média: {formatted_average}")
    print(separator)


def main():
    # ----------------------------------------------------------------------
    # Purpose: This script calculates the simple arithmetic average grade for a 
    # student based on predefined disciplines for study years 5 through 9. 
    # It demonstrates the use of auxiliary functions, conditional logic, and 
    # loop control without 'break'.
    # ----------------------------------------------------------------------

    print("--- Welcome to the Student Grade Calculator ---")

    # 1. Get input data
    student_name, study_year, all_grades_data = get_student_data()

    # 2. Calculate the average
    avg_grade = calculate_average(all_grades_data)

    # 3. Display the final results
    display_results(student_name, study_year, all_grades_data, avg_grade)

    print("\n--- Program finished. ---")


if __name__ == "__main__":
    main()
