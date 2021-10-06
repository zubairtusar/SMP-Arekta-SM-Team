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
