package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

//ParsedReturn is the return of the HTML parsed
type ParsedReturn struct {
	Title         string   `json:"name"`
	Description   string   `json:"description"`
	CreatedBy     string   `json:"created_by"`
	ReleasedAt    string   `json:"released_at"`
	Repositories  int64    `json:"repositories"`
	RelatedTopics []string `json:"related_topics"`
}

func main() {
	_ = parseHTML("golang.html")
}

func parseHTML(page string) error {
	r, err := os.Open("golang.html")
	if err != nil {
		return err
	}

	doc, err := goquery.NewDocumentFromReader(r)
	if err != nil {
		log.Fatal(err)
	}

	var createdBy, repositories string
	answer := ParsedReturn{}
	relatedTopics := []string{}

	doc.Find(".py-6").Each(func(i int, s *goquery.Selection) {
		title := s.Find("h1").Text()
		description := s.Find("p").Text()

		//tmpsplit := strings.Split(description, ".")
		//description = tmpsplit[0]

		geral := s.Find(".list-style-none .d-md-inline-block ").Has("span").Text()

		//Split the strings "Created By" and "Released"
		splited := strings.Split(geral, "Released ")
		releasedAt := strings.TrimSpace(splited[1])
		createdBy = strings.TrimSpace(strings.Replace(splited[0], "Created by", " ", -1))
		repositories = strings.Replace(doc.Find(".d-md-flex").Find("h2 .Counter").Text(), ",", "", -1)

		//Prints for testing
		/*fmt.Printf("title:%s\n", title)
		fmt.Printf("description:%s\n", description)
		fmt.Printf("released_at:%s", releasedAt)
		fmt.Printf("created_by:%s\n", createdBy)
		*/
		repositoriesInt, err := strconv.ParseInt(repositories, 10, 64)
		if err != nil {
			panic(err)
		}
		//	fmt.Printf("repositories:%d\n", repositoriesInt)

		doc.Find("div .col-md-4 .topic-tag").Each(func(i int, s *goquery.Selection) {
			relatedTopics = append(relatedTopics, strings.TrimSpace(s.Text()))
		})

		answer = ParsedReturn{title, description, createdBy, releasedAt, repositoriesInt, relatedTopics}

		//answerjson, err := json.MarshalIndent(answer, "", " ")
		answerjson, err := json.Marshal(answer)
		if err != nil {
			panic(err)
		}
		//fmt.Println(answerjson)

		ioutil.WriteFile("golang.json", answerjson, 0)
	})

	return nil
}
