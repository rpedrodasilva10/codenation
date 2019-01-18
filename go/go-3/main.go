package main

import (
	"database/sql"
	"encoding/json"
	"log"
	"net/http"
	"os"
	"strings"
	"time"

	"github.com/gorilla/context"
	"github.com/gorilla/mux"
	_ "github.com/mattn/go-sqlite3"
)

//PORT port to be used
const PORT = "8080"

//QuoteReturn defines a return of a quote
type QuoteReturn struct {
	Actor string `json:"actor"`
	Quote string `json:"quote"`
}

func main() {

	r := mux.NewRouter()
	http.Handle("/", r)
	r.Handle("/v1/quote", quote()).Methods("GET")

	//ByACTOR
	r.Handle("/v1/quote/{actor}", quoteByActor()).Methods("GET")

	logger := log.New(os.Stderr, "logger: ", log.Lshortfile)
	srv := &http.Server{
		ReadTimeout:  30 * time.Second,
		WriteTimeout: 30 * time.Second,
		Addr:         ":" + PORT,
		Handler:      context.ClearHandler(http.DefaultServeMux),
		ErrorLog:     logger,
	}
	err := srv.ListenAndServe()
	if err != nil {
		log.Fatal(err)
	}
}

func quote() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		//Open database
		db, errdb := sql.Open("sqlite3", "./database.sqlite")
		if errdb != nil {
			log.Fatal(errdb)
		}
		defer db.Close()
		if errdb != nil {
			log.Fatal(errdb)
		}
		answer := QuoteReturn{}
		actor := ""
		sqlCmd := "SELECT actor, detail from scripts where detail != ' ' and actor != ' '  ORDER BY RANDOM() LIMIT 1"
		rows, errdb := db.Query(sqlCmd)
		//	defer rows.Close()
		if errdb != nil {
			log.Fatal(errdb)
		}
		var detail string
		for rows.Next() {
			rows.Scan(&actor, &detail)
			break
		}
		answer = QuoteReturn{actor, detail}
		json.NewEncoder(w).Encode(answer)

	})
}

func quoteByActor() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		//w.WriteHeader(http.StatusNotImplemented)
		w.WriteHeader(http.StatusOK)
		// Abre conexão com banco
		// @todo - inserir numa função

		db, errdb := sql.Open("sqlite3", "./database.sqlite")

		if errdb != nil {
			log.Fatal(errdb)
		}
		if errdb != nil {
			log.Fatal(errdb)
		}

		answer := QuoteReturn{}
		params := mux.Vars(r)
		act := params["actor"]
		act = strings.Replace(act, "+", " ", -1)
		actResp := ""
		sqlCmd := "SELECT actor, detail from scripts where actor = " + "'" + act + "'"
		sqlCmd += " and detail != ' ' ORDER BY RANDOM() LIMIT 1"
		rows, errdb := db.Query(sqlCmd)
		defer rows.Close()
		if errdb != nil {
			log.Fatal(errdb)
		}
		var detail string
		for rows.Next() {
			rows.Scan(&actResp, &detail)
			break
		}
		answer = QuoteReturn{actResp, detail}
		json.NewEncoder(w).Encode(answer)

	})
}
