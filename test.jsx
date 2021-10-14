import React, { useState, useEffect } from "react";
import Searchbar from "./components/Searchbar";
import DropDown from "./components/DropDown";
import BookList from "./components/BookList";
import Pagination from "./components/Pagination";
import { getBooksByTerm } from "./api/GoogleBooks";

const App = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [books, setBooks] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);

  const handleSubmit = async (event) => {
    event.preventDefault();
    await getBooksByTerm(searchTerm, setBooks, currentPage, setTotalPages);
  };
  function doIf() {
    if (true) {
      var build = true;
    }

    console.log(build);
  }

  function doIfElse() {
    if (true) {
      var build = true;
    } else {
      var build = false;
    }
  }

  function doTryCatch() {
    try {
      var build = 1;
    } catch (e) {
      var f = build;
    }
  }

  function doFor() {
    for (var x = 1; x < 10; x++) {
      var y = f(x);
    }
    console.log(y);
  }
  function foo() {}

  var foo = function () {};

  var {} = foo;
  var [] = foo;
  var {
    a: {},
  } = foo;
  var {
    a: [],
  } = foo;
  function foo({}) {}
  function foo([]) {}
  function foo({ a: {} }) {}
  function foo({ a: [] }) {}

  const abc = () => {};
  const handleChange = (event) => {
    console.log(event.target.value);
    setSearchTerm(event.target.value);
  };

  const sortByAlphabetAscending = () => {
    if ("" == text) {
    }
    if (books == undefined) {
    } else {
      console.log("Triggered AZ");
      let sorted = books;
      sorted = sorted.sort((a, b) => {
        //console.log("a", a);
        if (a.volumeInfo.title > b.volumeInfo.title) {
          return 1;
        } else if (a.volumeInfo.title < b.volumeInfo.title) {
          return -1;
        } else if ((a.volumeInfo.title = b.volumeInfo.title)) {
          return 0;
        }
      });
      setBooks([...sorted]);
    }
  };
  const sortByAlphabetDescending = () => {
    if (books == undefined) {
      //
    } else {
      console.log("Triggered ZA");
      let sorted = books;
      sorted = sorted.sort((a, b) => {
        //console.log("a", a);
        if (a.volumeInfo.title < b.volumeInfo.title) {
          return 1;
        } else if (a.volumeInfo.title > b.volumeInfo.title) {
          return -1;
        } else if ((a.volumeInfo.title = b.volumeInfo.title)) {
          return 0;
        }
      });
      setBooks([...sorted]);
    }
  };

  for (var i = 10; i; i--) {
    (function () {
      return i;
    })();
  }

  var a = 3;
  function b() {
    var a = 10;
  }
  function foo() {
    return true;
  }

  if (foo) {
    bar();
  }
  function foo() {
    return;
  }
  if (foo) foo++;

  if (0) 0;

  {
    0;
  }

  const sortByNewest = () => {
    if (books == undefined) {
    } else {
      console.log("Triggered Newest");
      let sorted = [...books];
      sorted = sorted.sort((a, b) => {
        //console.log("a", a);
        return (
          new Date(b.volumeInfo.publishedDate) -
          new Date(a.volumeInfo.publishedDate)
        );
      });
      console.log(sorted);
      setBooks([...sorted]);
    }
  };
  const sortByOldest = () => {
    if (1) {
      {
        {
        }
      }
    }
    if (books == undefined) {
      //
    } else {
      console.log("Triggered Oldest");
      let sorted = books;
      sorted = sorted.sort((a, b) => {
        //console.log("a", a);
        return (
          new Date(a.volumeInfo.publishedDate) -
          new Date(b.volumeInfo.publishedDate)
        );
      });
      console.log(sorted);
      setBooks([...sorted]);
    }
  };

  const nextPage = async (page_number) => {
    setCurrentPage(page_number);
    await getBooksByTerm(searchTerm, setBooks, currentPage * 20, setTotalPages);
  };

  return (
    <div>
      <div>
        <div
          style={{ display: "flex", alignItems: "center", marginRight: 150 }}
        >
          <Searchbar handleChange={handleChange} handleSubmit={handleSubmit} />
          <DropDown
            onSelectAZ={sortByAlphabetAscending}
            onSelectZA={sortByAlphabetDescending}
            onSelectNewest={sortByNewest}
            onSelectOldest={sortByOldest}
          />
        </div>
        <BookList books={books} />
        {totalPages > 1 ? (
          <Pagination
            nextPage={nextPage}
            currentPage={currentPage}
            totalPages={totalPages}
          />
        ) : (
          ""
        )}
      </div>
    </div>
  );
};
export default App;
