package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

type Resposta struct {
	arquivosresposta []File
}

type File struct {
	Name string `json:"name"`
	Path string `json:"path"`
}

var arquivo Resposta

func main() {
	//@todo read dir name from stdin
	args := os.Args[1:]
	_ = jsonify(args[0])
}

var finalstruct File

func jsonify(dir string) error {
	var files []string
	root := dir
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		files = append(files, path)
		return nil
	})
	if err != nil {
		panic(err)
	}
	for _, file := range files {
		filename := filepath.Base(file)
		path := filepath.Dir(file)
		if strings.Contains(file, ".txt") {
			//fmt.Println("Name:", filename, "Path:", "./"+path+"/"+filename)
			arquivo.arquivosresposta = append(arquivo.arquivosresposta, File{filename, "./" + path + "/" + filename})

		}
	}
	b, _ := json.Marshal(arquivo.arquivosresposta)
	c := []byte(b)
	ioutil.WriteFile("files.json", c, 0644)
	return nil
}
