**Project Title**

**Library Management System**

Problem Statement

Many small libraries (classroom libraries, club libraries, and personal collections) lack a lightweight, easy-to-run tool to track books, borrowers, issues and returns. The goal of this project is to build a simple, CLI-based library management system that demonstrates CRUD operations, basic reporting, and modular code design suitable for extension and evaluation.

**Target Users**

School/college classroom teachers running small reading corners

Student clubs managing a few books

Beginners learning software engineering principles and version control

**Scope of the Project**

Implement an in-memory CLI application supporting book and borrower management, issuing/returning books, and basic reports.

Provide clear documentation (README.md and statement.md) to satisfy the VITyarthi BuildYourOwnProject template.

Deliver code organized for easy extension (persistence, GUI, or web API).

High-level Features

Book management (add, list, search)

Borrower management (add)

Issue / Return flow with availability tracking

Reports: available books, currently issued books, borrower history

Simple, human-readable ID generation (B1, U1, I1)

**Functional Requirements** 

**User Management Module**

Add borrower

Validate borrower IDs

Book Management Module

Add book

List books

Search books by title/author

**Issue Management Module**

Issue book to borrower (decrement available copies)

Return book (increment available copies)

Track issue records and returned status

**Reporting Module**

Available books

Issued books

Borrower history

Non-Functional Requirements 

Usability: Simple CLI with numbered menu for easy evaluation.

Reliability: Prevent double-returns and issuing when no copies are available.

Maintainability: Modular functions and clear inline comments for easy extension.

Performance: Lightweight in-memory operations suitable for small datasets.

Error handling: Validate numeric input and IDs; provide informative messages.

**System Architecture**

Single-process CLI Python app

In-memory data structures (dictionaries) as the primary storage model

Modules/functions map to features (books, borrowers, issues, reports)


**Data Model (summary)**

books : { book_id -> { title, author, copies_total, copies_available } }

borrowers : { borrower_id -> { name } }

issues : { issue_id -> { book_id, borrower_id, returned } }

Implementation Details (brief)

Language: Python 3.8+

Code organization: src/LMS.py contains the CLI and functions

ID generation strategy: simple incremental IDs prefixed by type (B/U/I)

No external libraries required (standard library only)

**Testing Strategy**

Manual interactive testing following these test cases:

Add a book -> verify listing and availability

Add borrower -> verify borrower ID

Issue book when copies exist -> copies decrement and issue record created

Attempt to issue when no copies available -> operation blocked

Return book -> returned flag set and copies incremented

Attempt to return already returned issue -> operation blocked

Document sample runs and include screenshots in the PDF report.

**Future Enhancement**s

JSON/CSV or SQLite persistence to save state between runs

Web or GUI frontend

Authentication & role-based access (librarian vs. borrower)

Enhanced search (fuzzy matching) and sorting
