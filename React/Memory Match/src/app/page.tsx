"use client";
import Image from "next/image";
import styles from "./page.module.css";
import { useEffect, useState } from "react";

export default function Home() {

    // Lógica do jogo
  const emojis = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼'];
  const [cards, setCards] = useState<{ face: string; flipped: boolean }[]>([]);
  const [moves, setMoves] = useState(0);
  const [gameWon, setGameWon] = useState(false);
  const [selectedCards, setSelectedCards] = useState<number[]>([]);

  useEffect(() => {
    restartGame();
  }, []);

  const restartGame = () => {
    const pairedCards = [...emojis, ...emojis]
      .map((face) => ({ face, flipped: false }))
      .sort(() => Math.random() - 0.5);
    setCards(pairedCards);
    setMoves(0);
    setGameWon(false);
  };

  const flipCard = (index: number) => {
  if (
    cards[index].flipped || 
    gameWon || 
    selectedCards.length >= 2 || 
    selectedCards.includes(index)
  ) return;

  const newCards = [...cards];
  newCards[index] = { ...newCards[index], flipped: true };
  setCards(newCards);
  setSelectedCards([...selectedCards, index]);

  // Verifica par quando 2 cartas estão viradas
  if (selectedCards.length === 1) {
    const [firstIndex] = selectedCards;
    if (cards[firstIndex].face === newCards[index].face) {
      // Par encontrado - limpa seleção
      setSelectedCards([]);
    } else {
      // Par errado - desvira após 1s
      setTimeout(() => {
        setCards(prevCards => {
          const resetCards = [...prevCards];
          resetCards[firstIndex] = { ...resetCards[firstIndex], flipped: false };
          resetCards[index] = { ...resetCards[index], flipped: false };
          return resetCards;
        });
        setSelectedCards([]);
      }, 1000);
    }
    setMoves(moves + 1);
  }
};

  useEffect(() => {
    if (cards.length > 0 && cards.every((card) => card.flipped)) {
      setGameWon(true);
    }
  }, [cards]);

  return (
  <div className={styles.page}>
    <div className={styles.description}>
      {/* Header mantido igual */}
    </div>

    <main className={styles.main}>
      <h1>Memory Match</h1>
      <p>Moves: {moves}</p>

      <div className={styles.board}>
        {cards.map((card, index) => (
          <button
            key={index}
            className={`${styles.card} ${card.flipped ? styles.flipped : ''}`}
            onClick={() => flipCard(index)}
            aria-label={`Card ${index}`}
          >
            <div className={styles.cardContent}>
              {card.flipped ? card.face : 'X'}
            </div>
          </button>
        ))}
      </div>

      <button 
        onClick={restartGame} 
        className={styles.button}
        aria-label="Restart game"
      >
        Restart
      </button>
      
      {gameWon && (
        <div className={styles.winMessage}>
          <p>You won in {moves} moves! 🎉</p>
        </div>
      )}
    </main>

    <footer className={styles.footer}>
      {/* Footer mantido igual */}
    </footer>
  </div>
);
}
