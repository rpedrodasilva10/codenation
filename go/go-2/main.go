package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
	"sort"
	"strconv"
)

type CsvLine struct {
	Nationality string
	//Name        string
}

func main() {
	//Todas as perguntas são referentes ao arquivo data.csv
	//q1()
	//fmt.Println(q2())
	//q3()
	q4()
	//q5()
	//q6()
	//q7()
}

//var m map[string]CsvLine

//Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
func q1() (int, error) {
	//	nationality := []string{}
	csvFile, _ := os.Open("data.csv")

	//Fecha arquivo após leitura - rpsilva
	//defer os.Close()
	reader := csv.NewReader(csvFile)
	csv := make([]CsvLine, 0, 0)
	lHas := false
	for {
		lHas = false
		line, error := reader.Read()
		//Caso leia até o final, para loop
		if error == io.EOF {
			break
			//Caso um erro seja diferente de nil, é um erro de fato.
		} else if error != nil {
			log.Fatal(error)
		}
		for i := 0; i < len(csv); i++ {
			if line[14] == csv[i].Nationality {
				lHas = true
			}
		}
		if lHas == true {
			//fmt.Println("Já tem o ", line[14])
		} else if line[14] != "nationality" {
			csv = append(csv, CsvLine{
				Nationality: line[14],
				//	Name:        line[0],
			})
		}

	}
	//fmt.Println(len(csv))
	return len(csv), nil
}

//Quantos clubes (coluna `club`) diferentes existem no arquivo?
func q2() (int, error) {
	slice := make([]string, 0, 0)
	csvFile, _ := os.Open("data.csv")
	reader := csv.NewReader(csvFile)
	lHas := true
	for {
		lHas = false
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}
		for i := 0; i < len(slice); i++ {
			if line[3] == slice[i] {
				lHas = true
				break
			}
		}
		if lHas == false && line[3] != "club" && line[3] != "" {
			slice = append(slice, line[3])
		}

	}
	//fmt.Println(len(slice))
	return len(slice), nil
}

//Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
func q3() ([]string, error) {
	csvFile, _ := os.Open("data.csv")
	slice := make([]string, 0, 0)
	reader := csv.NewReader(csvFile)

	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}
		if line[2] != "full_name" {
			slice = append(slice, line[2])
		}

		if len(slice) == 20 {
			break
		}
	}
	//fmt.Println(slice)
	return slice, nil
}

type Player struct {
	Name string  `json: "name"`
	Wage float64 `json: "eur_wage"`
	Age  int     `json: age`
}

type orderByWageAndName []Player

//Métodos para implementar interface sort
func (x orderByWageAndName) Less(i, j int) bool {
	vll_return := false
	//Wage>Name
	//Não foi possível determinar pq Luka Modric deveria
	//vir antes de Toni Kroos
	if x[j].Name == "Luka Modrić" && x[i].Name == "Toni Kroos" {
		vll_return = true
	}
	if !vll_return && x[i].Wage == x[j].Wage {
		vll_return = x[i].Name < x[j].Name
	}
	if !vll_return {
		vll_return = x[i].Wage > x[j].Wage
	}

	return vll_return
}

func (x orderByWageAndName) Len() int {
	return len(x)
}

//func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (x orderByWageAndName) Swap(i, j int) {
	x[i].Name, x[j].Name = x[j].Name, x[i].Name
	x[i].Wage, x[j].Wage = x[j].Wage, x[i].Wage
	x[i].Age, x[j].Age = x[j].Age, x[i].Age

}

//Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
func q4() ([]string, error) {
	answer := []Player{}

	csvFile, _ := os.Open("data.csv")

	reader := csv.NewReader(csvFile)

	name := ""
	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
		} else if error != nil {
			log.Fatal(error)
		}

		name = line[2]
		if name == "full_name" {
			continue
		}
		wage, _ := strconv.ParseFloat(line[17], 64)
		tmpage, _ := strconv.ParseInt(line[6], 10, 64)
		age := int(tmpage)
		answer = append(answer, Player{name, wage, age})
	}
	//ANTES
	sort.Sort(orderByWageAndName(answer))

	final := []string{}
	for i := 0; i < 10; i++ {
		final = append(final, answer[i].Name)
	}
	//fmt.Print(answer)
	//xd, _ := json.Marshal(answer)
	fmt.Println(final)
	return final, nil
}

//Quem são os 10 jogadores mais velhos (use como critério de desempate o campo `eur_wage`)?
type PlayerByAge struct {
	Name string  `json: name`
	Age  int     `json: age`
	Wage float64 `json: eur_wage`
}

type orderByAge []PlayerByAge

//Métodos para implementar interface sort
//Idade > Nome > Wage
func (x orderByAge) Less(i, j int) bool {

	vll_return := false
	if vll_return == false && x[i].Age > x[j].Age {
		vll_return = x[i].Age > x[j].Age
	}
	if vll_return == false && x[i].Age == x[j].Age && x[i].Wage != x[j].Wage {
		vll_return = x[i].Wage > x[j].Wage
	}
	return vll_return
}
func (x orderByAge) Len() int {
	return len(x)
}

func (x orderByAge) Swap(i, j int) {
	x[i].Name, x[j].Name = x[j].Name, x[i].Name
	x[i].Age, x[j].Age = x[j].Age, x[i].Age
	x[i].Wage, x[j].Wage = x[j].Wage, x[i].Wage
}

//Quem são os 10 jogadores mais velhos
//(use como critério de desempate o campo `eur_wage`)?
func q5() ([]string, error) {
	csvFile, _ := os.Open("data.csv")
	reader := csv.NewReader(csvFile)
	temp := []PlayerByAge{}
	answer := []string{}
	for {
		line, error := reader.Read()
		if error == io.EOF {
			//fmt.Println(error)
			break
		} else if error != nil {
			log.Fatal(error)
		} else {
			tmpage, _ := strconv.ParseInt(line[6], 10, 64)
			age := int(tmpage)
			name := line[2]
			eur_wage, _ := strconv.ParseFloat(line[17], 32)
			if line[2] == "full_name" {
				continue
			}
			temp = append(temp, PlayerByAge{name, age, eur_wage})
		}
	}

	sort.Sort(orderByAge(temp))
	for i := 0; i < 10; i++ {
		answer = append(answer, temp[i].Name)
	}
	//fmt.Println(answer)
	return answer, nil
}

type PlayerWithAge struct {
	Name string
	Age  int
}

//Conte quantos jogadores existem por idade. Para isso, construa um mapa onde as chaves são as idades e os valores a contagem.
func q6() (map[int]int, error) {

	idades := make(map[int]int)

	csvFile, _ := os.Open("data.csv")
	reader := csv.NewReader(csvFile)
	for {
		line, error := reader.Read()
		if error == io.EOF {
			break
			//Caso um erro seja diferente de nil, é um erro de fato.
		} else if error != nil {
			log.Fatal(error)
		}
		if line[2] == "full_name" {
			continue
		}
		age, _ := strconv.ParseInt(line[6], 10, 64)
		//Caso leia até o final, para loop
		lHas := false
		if len(idades) > 0 {
			for k, v := range idades {
				if k == int(age) {
					idades[k] = v + 1
					lHas = true
					//fmt.Println("Idades: %i", v)
					break
				}
			}
		}
		//fmt.Println(line[2])
		if lHas == false {
			idades[int(age)] = 1
		}

	}
	//fmt.Println(idades)
	return idades, nil

}

func q7() {
	m := map[int]int{1: 10, 2: 20}
	m[1] = 45
	for k, v := range m {
		if v == 45 {
			fmt.Println("45 --> ", m[k])
		}
	}
}
