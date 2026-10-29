// Build the Remon Motion Studio Blueprint .docx from sec/*.md
const fs = require('fs');
const path = require('path');
const D = require('/opt/npm-tools/node_modules/docx');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, Header, Footer, PageNumber,
  TableOfContents, LevelFormat, PageBreak, TableLayoutType, VerticalAlign,
} = D;

const DIR = __dirname;
const OUT = process.argv[2] || path.join(DIR, 'out.docx');
const NAVY = '17365D', SLATE = '44546A', TEXT = '111111', LIGHT = 'EEF2F8', LINE = 'C9D3E3';
const FONT = 'Aptos';
const PAGE_W = 11906, MARGIN = 1300, CONTENT_W = PAGE_W - 2 * MARGIN; // A4

const meta = JSON.parse(fs.readFileSync(path.join(DIR, 'meta.json'), 'utf8'));

// ---------- inline **bold** ----------
function runs(text, opts = {}) {
  const parts = text.split(/(\*\*[^*]+\*\*)/g).filter(s => s !== '');
  return parts.map(p => {
    const b = p.startsWith('**') && p.endsWith('**');
    return new TextRun({ text: b ? p.slice(2, -2) : p, bold: b || opts.bold, color: opts.color, size: opts.size, font: FONT });
  });
}

// ---------- tables ----------
function splitRow(line) {
  let s = line.trim();
  if (s.startsWith('|')) s = s.slice(1);
  if (s.endsWith('|')) s = s.slice(0, -1);
  return s.split('|').map(c => c.trim());
}
function makeTable(rows) {
  const header = rows[0];
  const body = rows.slice(1);
  const n = header.length;
  const norm = body.map(r => { const x = r.slice(0, n); while (x.length < n) x.push(''); return x; });
  // widths proportional to sqrt of max length, min share
  const lens = header.map((h, i) => Math.max(h.length, ...norm.map(r => r[i].length), 3));
  const weights = lens.map(l => Math.sqrt(Math.min(l, 120)));
  const tot = weights.reduce((a, b) => a + b, 0);
  let widths = weights.map(w => Math.max(700, Math.round(CONTENT_W * w / tot)));
  const sum = widths.reduce((a, b) => a + b, 0);
  widths = widths.map(w => Math.round(w * CONTENT_W / sum));
  widths[widths.length - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  const borders = { top: border, bottom: border, left: border, right: border };
  const cell = (t, i, isHead, zebra) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    borders,
    shading: isHead ? { type: ShadingType.CLEAR, color: 'auto', fill: NAVY } : (zebra ? { type: ShadingType.CLEAR, color: 'auto', fill: 'F6F8FB' } : undefined),
    margins: { top: 50, bottom: 50, left: 90, right: 90 },
    verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ spacing: { before: 0, after: 0, line: 252 }, children: runs(t, { bold: isHead, color: isHead ? 'FFFFFF' : TEXT, size: 17 }) })],
  });
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    rows: [
      new TableRow({ tableHeader: true, cantSplit: true, children: header.map((h, i) => cell(h, i, true, false)) }),
      ...norm.map((r, k) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, i, false, k % 2 === 1)) })),
    ],
  });
}

// ---------- markdown → blocks ----------
let numInstance = 0;
function mdToBlocks(md) {
  const lines = md.replace(/\r/g, '').split('\n');
  const out = [];
  let i = 0, firstH1 = true, lastWasNum = false;
  while (i < lines.length) {
    const line = lines[i];
    const t = line.trim();
    if (!t) { i++; lastWasNum = false; continue; }
    if (t.startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        const r = lines[i].trim();
        if (!/^\|?\s*:?-{2,}/.test(r.replace(/\|/g, '|'))) {
          if (!/^\|[\s:|-]+\|?$/.test(r)) rows.push(splitRow(r));
        }
        i++;
      }
      if (rows.length) { out.push(makeTable(rows)); out.push(new Paragraph({ spacing: { before: 0, after: 120 }, children: [] })); }
      continue;
    }
    let m;
    if ((m = t.match(/^(#{1,3})\s+(.*)$/))) {
      const lvl = m[1].length;
      const text = m[2].trim();
      if (lvl === 1) {
        out.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: runs(text) }));
      } else if (lvl === 2) {
        out.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(text) }));
      } else {
        out.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: runs(text) }));
      }
      i++; lastWasNum = false; continue;
    }
    if (t.startsWith('> ')) {
      out.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, color: 'auto', fill: LIGHT },
        border: { left: { style: BorderStyle.SINGLE, size: 24, color: NAVY, space: 8 } },
        indent: { left: 200, right: 120 },
        spacing: { before: 120, after: 160, line: 276 },
        children: runs(t.slice(2)),
      }));
      i++; lastWasNum = false; continue;
    }
    if ((m = line.match(/^(\s*)[-*]\s+(.*)$/))) {
      const lvl = m[1].length >= 2 ? 1 : 0;
      out.push(new Paragraph({ numbering: { reference: 'bul', level: lvl }, spacing: { before: 0, after: 60 }, children: runs(m[2]) }));
      i++; continue;
    }
    if ((m = line.match(/^(\s*)\d+[.)]\s+(.*)$/))) {
      if (!lastWasNum) numInstance++;
      const lvl = m[1].length >= 2 ? 1 : 0;
      out.push(new Paragraph({ numbering: { reference: 'num', level: lvl, instance: numInstance }, spacing: { before: 0, after: 60 }, children: runs(m[2]) }));
      lastWasNum = true; i++; continue;
    }
    // paragraph (join soft-wrapped lines)
    let txt = t; i++;
    while (i < lines.length && lines[i].trim() && !/^(#|\||> |\s*[-*]\s|\s*\d+[.)]\s)/.test(lines[i])) { txt += ' ' + lines[i].trim(); i++; }
    out.push(new Paragraph({ spacing: { before: 0, after: 140, line: 288 }, children: runs(txt) }));
    lastWasNum = false;
  }
  return out;
}

// ---------- cover ----------
function cover() {
  const box = new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill: NAVY },
      borders: { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } },
      margins: { top: 500, bottom: 500, left: 500, right: 500 },
      children: [
        new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: meta.title1, bold: true, size: 56, color: 'FFFFFF', font: FONT })] }),
        new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: meta.title2, size: 56, color: 'FFFFFF', font: FONT })] }),
        new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: meta.subtitle, size: 24, color: 'DCE4F0', font: FONT })] }),
        new Paragraph({ children: [new TextRun({ text: meta.tagline, size: 20, color: 'DCE4F0', font: FONT, characterSpacing: 40 })] }),
      ],
    })] })],
  });
  const kv = meta.coverRows.map(([k, v]) => [k, v]);
  const w1 = 2200, w2 = CONTENT_W - w1;
  const border = { style: BorderStyle.SINGLE, size: 4, color: LINE };
  const borders = { top: border, bottom: border, left: border, right: border };
  const info = new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [w1, w2],
    rows: kv.map(([k, v]) => new TableRow({ children: [
      new TableCell({ width: { size: w1, type: WidthType.DXA }, borders, shading: { type: ShadingType.CLEAR, color: 'auto', fill: LIGHT }, margins: { top: 60, bottom: 60, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: k, bold: true, size: 18, color: NAVY, font: FONT })] })] }),
      new TableCell({ width: { size: w2, type: WidthType.DXA }, borders, margins: { top: 60, bottom: 60, left: 100, right: 100 }, children: [new Paragraph({ children: [new TextRun({ text: v, size: 18, font: FONT })] })] }),
    ] })),
  });
  return [
    new Paragraph({ spacing: { before: 1400, after: 200 }, children: [new TextRun({ text: meta.company.toUpperCase(), bold: true, size: 20, color: NAVY, font: FONT, characterSpacing: 60 })] }),
    box,
    new Paragraph({ spacing: { before: 200, after: 300 }, children: [new TextRun({ text: meta.coverLine, size: 18, color: SLATE, font: FONT })] }),
    info,
    new Paragraph({ spacing: { before: 400 }, children: [new TextRun({ text: meta.disclaimer, size: 16, color: '666666', font: FONT })] }),
  ];
}

// ---------- assemble ----------
const order = JSON.parse(fs.readFileSync(path.join(DIR, 'order.json'), 'utf8'));
const front = mdToBlocks(fs.readFileSync(path.join(DIR, 'sec', 'front.md'), 'utf8'));
// contents
const body = [];
const heads = [];
for (const f of order) {
  const md = fs.readFileSync(path.join(DIR, 'sec', f), 'utf8');
  for (const l of md.split('\n')) { const m = l.match(/^(#{1,2})\s+(.*)$/); if (m) heads.push([m[1].length, m[2].replace(/\*\*/g, '').trim()]); }
  body.push(...mdToBlocks(md));
}
fs.writeFileSync(path.join(DIR, 'heads.json'), JSON.stringify(heads));
let pages = {};
try { pages = JSON.parse(fs.readFileSync(path.join(DIR, 'toc_pages.json'), 'utf8')); } catch (e) {}
const contents = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: 'Contents', font: FONT })] }),
  ...heads.map(([lvl, t], k) => new Paragraph({
    spacing: { before: lvl === 1 ? 100 : 0, after: lvl === 1 ? 30 : 10 },
    indent: { left: lvl === 1 ? 0 : 360 },
    tabStops: [{ type: D.TabStopType.RIGHT, position: CONTENT_W, leader: 'dot' }],
    children: [
      new TextRun({ text: t, bold: lvl === 1, size: lvl === 1 ? 19 : 17, color: lvl === 1 ? NAVY : TEXT, font: FONT }),
      new TextRun({ children: [new D.Tab()], size: lvl === 1 ? 19 : 17, font: FONT }),
      new TextRun({ text: String(pages[k] || '00'), bold: lvl === 1, size: lvl === 1 ? 19 : 17, font: FONT }),
    ],
  })),
];

const headerP = new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 4 } }, children: [
  new TextRun({ text: 'REMONLOGIC  /  ', bold: true, size: 15, color: NAVY, font: FONT, characterSpacing: 30 }),
  new TextRun({ text: 'REMON MOTION STUDIO BLUEPRINT', size: 15, color: SLATE, font: FONT, characterSpacing: 30 }),
] });
const footerP = new Paragraph({ style: 'FooterText', alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 4 } }, children: [
  new TextRun({ text: `Strictly Confidential  •  Edition ${meta.edition}  •  Page `, size: 15, color: SLATE, font: FONT }),
  new TextRun({ children: [PageNumber.CURRENT], size: 15, color: SLATE, font: FONT }),
  new TextRun({ text: ' of ', size: 15, color: SLATE, font: FONT }),
  new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 15, color: SLATE, font: FONT }),
] });

const doc = new Document({
  creator: meta.company, title: meta.title1 + ' ' + meta.title2, description: meta.subtitle,
  styles: {
    default: { document: { run: { font: FONT, size: 21, color: TEXT } } },
    paragraphStyles: [
      { id: 'FooterText', name: 'Footer Text', basedOn: 'Normal', run: { size: 15, color: SLATE, font: FONT } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 34, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 0, after: 240 }, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 6 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 300, after: 120 }, outlineLevel: 1, keepNext: true } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 22, bold: true, color: SLATE, font: FONT }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2, keepNext: true } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [
      { level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } } } },
      { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 800, hanging: 260 } } } },
    ] },
    { reference: 'num', levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 300 } } } },
      { level: 1, format: LevelFormat.LOWER_LETTER, text: '%2)', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 820, hanging: 300 } } } },
    ] },
  ] },
  features: { updateFields: true },
  sections: [
    { properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: 1200, bottom: 1200, left: MARGIN, right: MARGIN } } }, children: cover() },
    { properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: 1300, bottom: 1200, left: MARGIN, right: MARGIN, header: 600, footer: 600 } } },
      headers: { default: new Header({ children: [headerP] }) }, footers: { default: new Footer({ children: [footerP] }) },
      children: [...front, ...contents, ...body] },
  ],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('wrote', OUT, b.length); });
