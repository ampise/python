const m1 = [[0, 2], [-2, -5]]
const m2 = [[6, -6], [3, 0]]
// -- Define shape of resulting matrix
let m3 = [];

if (m1[0].length == m2.length) {
    let m1Row = 0;
    while (m1Row < m1.length) {
        m3.push([]);
        let m2Column = 0;
        while (m2Column < m2[m1Row].length) {
            let mm = 0;
            m1[m1Row].forEach((e, i) => {
                let m1Element = e;
                let m2Element = m2[i][m2Column];
                mm += (m1Element * m2Element);
            });
            m3[m1Row][m2Column] = mm;
            m2Column++;
        }; // loop over m2 columns
        m1Row++;
    }; // loop over m1 rows
    console.log(m3);
} // validate matrix dimensions fit
else {
    console.log("Sorry! The dimensions of the matrices don't match.")
}
