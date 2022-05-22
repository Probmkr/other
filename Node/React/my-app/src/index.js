import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function Square(props) {
  return (
    <button className="square" onClick={props.onClick} id={props.id}>
      {props.value}
    </button>
  );
}

function calculateWinner(squares, line = false) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return line ? lines[i] : squares[a];
    }
  }
}

class Board extends React.Component {
  renderSquare(i) {
    return (
      <Square
        value={this.props.squares[i]}
        onClick={() => { this.props.onClick(i); }}
        id={i}
      />
    );
  }

  render() {
    const board = [];
    for (let i = 0; i < 3; i++) {
      const squares = [];
      for (let j = 0; j < 3; j++) {
        squares.push(this.renderSquare(j + (i*3)));
      }
      board.push(<div className="board-row">{squares}</div>);
    }
    return (
      <div>
        {board}
      </div>
    );
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      history: [{
        squares: Array(9).fill(null),
      }],
      news: [],
      stepNumber: 0,
      xIsNext: true,
    }
  }

  handleClick(i) {
    const history = this.state.history.slice(0, this.state.stepNumber + 1);
    const news = this.state.news.slice(0, this.state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      history: history.concat([{
        squares: squares,
      }]),
      clicked: null,
      news: news.concat(i),
      stepNumber: history.length,
      xIsNext: !this.state.xIsNext,
    });
  }

  jumpTo(step) {
    this.setState({
      clicked: step,
      stepNumber: step,
      xIsNext: (step % 2) === 0,
    })
  }

  render() {
    const history = this.state.history;
    const current = history[this.state.stepNumber];
    const news = this.state.news;
    const winner = calculateWinner(current.squares);

    const moves = history.map((step, move) => {
      const newCol = news[move - 1] % 3 + 1;
      const newRow = Math.floor(news[move - 1] / 3) + 1;
      const desc = move ?
        'Go to move #' + move + ' ' + (move % 2 ? 'X' : 'O') + '( ' + newCol + ', ' + newRow + ' )' :
        'Go to game start';
      return (
        <li key={move}>
          <button className={this.state.clicked === move ? "selected" : null} onClick={() => this.jumpTo(move)}>{desc}</button>
        </li>
      );
    });

    for (let i = 0; i < 9; i++) {
      try {
      document.getElementById(i).classList.remove("selected");
      } catch (e) {
      }
    }

    let status;
    if (winner) {
      calculateWinner(current.squares, true).forEach(cell => {
        document.getElementById(cell).classList.add('selected');
      });
      status = 'Winner: ' + winner;
    } else if (this.state.stepNumber === 9) {
      status = 'Draw';
    } else {
      status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
    }

    return (
      <div className="game">
        <div className="game-board">
          <Board
            squares={current.squares}
            onClick={(i) => { this.handleClick(i); }}
          />
        </div>
        <div className="game-info">
          <div>{status}</div>
          <ol>{moves}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
