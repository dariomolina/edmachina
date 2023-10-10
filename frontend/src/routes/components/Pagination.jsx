import React from 'react'

export const Pagination = ({ totalPages, page, setPage }) => {
  return (
    <>
    <nav aria-label="Page navigation example">
      <ul className="pagination justify-content-center">
        <li className={`page-item ${page === 1 ? 'disabled' : ''}`}>
          <button className="page-link" onClick={() => setPage(page - 1)}>Previous</button>
        </li>
        {Array.from({ length: totalPages }, (_, i) => (
          <li className={`page-item ${i + 1 === page ? 'active' : ''}`} key={i}>
            <button className="page-link" onClick={() => setPage(i + 1)}>{i + 1}</button>
          </li>
        ))}
        <li className={`page-item ${page === totalPages ? 'disabled' : ''}`}>
          <button className="page-link" onClick={() => setPage(page + 1)}>Next</button>
        </li>
      </ul>
    </nav>
    </>
  )
}
