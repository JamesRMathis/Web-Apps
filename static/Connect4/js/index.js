function createBoard() {
    const board = document.getElementById("board-area")
    for (let i = 0; i < 6; i++) {
        const row = document.createElement("div")
        row.classList.add("row")

        for (let j = 0; j < 7; j++) {
            let cell = document.createElement("div")
            cell.classList.add("cell")

            if (0 < j) {
                cell.classList.add("no-left-border")
            }

            if (0 < i) {
                cell.classList.add("no-top-border")
            }

            cell.id = i + "_" + j

            cell.addEventListener("click", event => {
                const id = event.target.id
                const ids = id.split("_")
                let row = ids[0]
                let col = ids[1]

                if (document.getElementById(row + "_" + col).firstChild?.classList.contains("red") || document.getElementById(row + "_" + col).firstChild?.classList.contains("yellow")) {
                    return
                }

                while (row < 5 && !document.getElementById((parseInt(row) + 1) + "_" + col).firstChild?.classList.contains("red") && !document.getElementById((parseInt(row) + 1) + "_" + col).firstChild?.classList.contains("yellow")) {
                    row++
                }

                const cell = document.getElementById(row + "_" + col)
                const token = document.createElement("div")
                token.classList.add("token", redOrYellowTurn())
                cell.appendChild(token)
            })

            row.appendChild(cell)
        }
        board.appendChild(row)
    }
}

function redOrYellowTurn() {
    const cells = document.getElementsByClassName("cell")

    let filledCells = 0
    for (let i = 0; i < cells.length; i++) {
        const token = cells[i].firstChild

        if (token == null) {
            continue
        }

        if (token.classList.contains("red") || token.classList.contains("yellow")) {
            filledCells++
        }
    }

    if (filledCells % 2 == 1) {
        return "red"
    } else {
        return "yellow"
    }
}