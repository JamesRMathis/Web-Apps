numRows = 6
numCols = 7

function createBoard() {
    const board = document.getElementById("board-area")
    for (let i = 0; i < numRows; i++) {
        const row = document.createElement("div")
        row.classList.add("row")

        for (let j = 0; j < numCols; j++) {
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
                if (checkForWin() !== undefined) {
                    return
                }

                const id = event.target.id
                const ids = id.split("_")
                let row = parseInt(ids[0])
                let col = parseInt(ids[1])

                const token = document.getElementById(row + "_" + col).firstChild
                if (token?.classList.contains("red") || token?.classList.contains("yellow")) {
                    return
                }

                while (row < (numRows - 1) && !document.getElementById((row + 1) + "_" + col).firstChild?.classList.contains("red") && !document.getElementById((parseInt(row) + 1) + "_" + col).firstChild?.classList.contains("yellow")) {
                    row++
                }

                const cell = document.getElementById(row + "_" + col)
                const newToken = document.createElement("div")
                newToken.classList.add("token", redOrYellowTurn())
                cell.appendChild(newToken)

                const winner = checkForWin()
                if (winner != null) {
                    document.getElementById("winner").innerHTML = "<p>" + winner + " wins!</p>\n<button onclick=\"location.reload()\">Play again</button>"
                }
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

function checkForWin() {
    const cells = document.getElementsByClassName("cell")

    // Horizontal win
    for (let row = 0; row < numRows; row++) {
        let redCount = 0
        let yellowCount = 0

        for (let col = 0; col < numCols; col++) {
            const token = document.getElementById(row + "_" + col).firstChild

            if (token == null) {
                redCount = 0
                yellowCount = 0
                continue
            }

            if (token.classList.contains("red")) {
                redCount++
                yellowCount = 0
            } else {
                yellowCount++
                redCount = 0
            }

            if (redCount == 4) {
                return "red"
            } else if (yellowCount == 4) {
                return "yellow"
            }
        }
    }

    // Vertical win
    for (let col = 0; col < numCols; col++) {
        let redCount = 0
        let yellowCount = 0

        for (let row = 0; row < numRows; row++) {
            const token = document.getElementById(row + "_" + col).firstChild

            if (token == null) {
                redCount = 0
                yellowCount = 0
                continue
            }

            if (token.classList.contains("red")) {
                redCount++
                yellowCount = 0
            } else {
                yellowCount++
                redCount = 0
            }

            if (redCount == 4) {
                return "red"
            } else if (yellowCount == 4) {
                return "yellow"
            }
        }
    }

    // Diagonal win (top left to bottom right)
    for (let row = 0; row < numRows; row++) {
        let redCount = 0
        let yellowCount = 0

        for (let col = 0; col < numCols; col++) {
            const token = document.getElementById(row + "_" + col).firstChild

            if (token == null) {
                redCount = 0
                yellowCount = 0
                continue
            }

            if (token.classList.contains("red")) {
                redCount++
                yellowCount = 0
            } else {
                yellowCount++
                redCount = 0
            }

            if (redCount == 4) {
                return "red"
            } else if (yellowCount == 4) {
                return "yellow"
            }

            if (row < (numRows - 1) && col < (numCols - 1)) {
                const nextToken = document.getElementById((row + 1) + "_" + (col + 1)).firstChild
                if (nextToken == null) {
                    continue
                }

                if (token.classList.contains("red") && nextToken.classList.contains("red")) {
                    redCount = 2
                    yellowCount = 0
                } else if (token.classList.contains("yellow") && nextToken.classList.contains("yellow")) {
                    yellowCount = 2
                    redCount = 0
                } else {
                    redCount = 0
                    yellowCount = 0
                }
            }
        }
    }

    // Diagonal win (bottom left to top right)
    for (let row = numRows - 1; row >= 0; row--) {
        let redCount = 0
        let yellowCount = 0

        for (let col = 0; col < numCols; col++) {
            const token = document.getElementById(row + "_" + col).firstChild

            if (token == null) {
                redCount = 0
                yellowCount = 0
                continue
            }

            if (token.classList.contains("red")) {
                redCount++
                yellowCount = 0
            } else {
                yellowCount++
                redCount = 0
            }

            if (redCount == 4) {
                return "red"
            } else if (yellowCount == 4) {
                return "yellow"
            }

            if (row > 0 && col < (numCols - 1)) {
                const nextToken = document.getElementById((row - 1) + "_" + (col + 1)).firstChild
                if (nextToken == null) {
                    continue
                }

                if (token.classList.contains("red") && nextToken.classList.contains("red")) {
                    redCount = 2
                    yellowCount = 0
                } else if (token.classList.contains("yellow") && nextToken.classList.contains("yellow")) {
                    yellowCount = 2
                    redCount = 0
                } else {
                    redCount = 0
                    yellowCount = 0
                }
            }
        }
    }
}