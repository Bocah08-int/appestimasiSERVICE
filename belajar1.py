<!DOCTYPE html>
<html lang="id">
<head>
  <base target="_top">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Estimasi Servis Astra Daihatsu Urip</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
  
  <style>
    :root { --astra-blue: #004a99; --bg-light: #f4f7f9; }
    body { padding: 30px 15px; background-color: var(--bg-light); font-family: 'Inter', sans-serif; color: #334155; }
    
    .estimate-container { 
      max-width: 1000px; margin: auto; background: white; padding: 40px; border-radius: 16px;
      border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    }

    .brand-title { color: var(--astra-blue); font-weight: 800; font-size: 18px; text-transform: uppercase; margin-bottom: 0; }
    .branch-info { font-size: 11px; color: #64748b; line-height: 1.4; }
    .plat-box { background: #1e293b; color: white !important; padding: 10px 20px; font-weight: 800; border-radius: 8px; display: inline-block; min-width: 150px; text-align: center; }

    .section-card { border: 1px solid #f1f5f9; border-radius: 12px; padding: 20px; margin-bottom: 20px; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .info-label { width: 90px; display: inline-block; font-weight: 700; font-size: 10px; color: #94a3b8; letter-spacing: 0.5px; }
    .input-underlined { border: none; border-bottom: 1.5px solid #e2e8f0; font-weight: 600; font-size: 14px; width: calc(100% - 100px); outline: none; transition: 0.3s; }
    .input-underlined:focus { border-bottom-color: var(--astra-blue); }

    .table { font-size: 13px; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
    .table-header { background-color: #f8fafc !important; color: var(--astra-blue) !important; font-weight: 700; border-top: 3px solid var(--astra-blue); }
    
    .category-divider { background-color: #f1f5f9 !important; font-weight: 800; color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; padding: 10px 15px !important; }
    
    .row-jasa { background-color: #ffffff; }
    .row-part { background-color: #fafafa; }
    
    .badge-tag { font-size: 9px; padding: 3px 7px; border-radius: 4px; font-weight: 700; text-transform: uppercase; margin-right: 10px; border: 1px solid transparent; }
    .badge-jasa { background-color: #e0f2fe; color: #0369a1; border-color: #bae6fd; }
    .badge-part { background-color: #f0fdf4; color: #15803d; border-color: #bbf7d0; }

    .total-display { background: #ffcc00 !important; color: #000; border-radius: 12px; padding: 25px; text-align: right; box-shadow: inset 0 -3px 0 rgba(0,0,0,0.1); }
    .total-amount { font-size: 34px; font-weight: 900; display: block; margin-top: 5px; }
    
    .signature-name { border-bottom: 2px solid #000; display: inline-block; width: 220px; margin-top: 45px; font-weight: 800; text-transform: uppercase; font-size: 14px; }

    @media print {
      body { background: white; padding: 0; }
      .no-print { display: none !important; }
      .input-underlined { border-bottom: none; }
      .estimate-container { border: none; box-shadow: none; width: 100%; padding: 0; }
      .row-part { background-color: #fafafa !important; -webkit-print-color-adjust: exact; }
    }
  </style>
</head>
<body>

<div class="estimate-container">
  <div class="row mb-4 align-items-center">
    <div class="col-8">
      <p class="brand-title">PT Astra International Tbk - Daihatsu Sales Operation</p>
      <p class="branch-info"><strong>Makassar Urip</strong> | Jl. Urip Sumoharjo No. 64 | Telp: (0411) 449911</p>
    </div>
    <div class="col-4 text-end">
       <div class="plat-box">
         <input type="text" id="platNomor" class="bg-transparent border-0 text-center fw-bold text-white w-100" placeholder="NOMOR PLAT" style="outline:none;">
       </div>
    </div>
  </div>

  <div class="row g-3 mb-2">
    <div class="col-md-6">
      <div class="section-card shadow-sm">
        <h6 class="fw-bold mb-3 small text-primary text-uppercase">Data Pelanggan</h6>
        <div class="mb-2"><span class="info-label">NAMA</span><input type="text" id="userName" class="input-underlined" placeholder="Input Nama"></div>
        <div class="mb-2"><span class="info-label">CUSTOMER</span><input type="text" id="userPhone" class="input-underlined" placeholder="Nomor Telp/WA"></div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="section-card bg-light shadow-sm">
        <h6 class="fw-bold mb-3 small text-primary text-uppercase">Detail Unit</h6>
        <select id="typeSelect" class="form-select form-select-sm mb-2 fw-bold" onchange="updateTable()">
          <option value="">-- PILIH MODEL UNIT --</option>
          <option value="Xenia">Xenia</option><option value="Terios">Terios</option><option value="Ayla">Ayla</option><option value="Sigra">Sigra</option><option value="Grandmax">Grandmax</option><option value="Luxio">Luxio</option><option value="Rocky">Rocky</option>
        </select>
        <select id="categorySelect" class="form-select form-select-sm fw-bold" onchange="updateTable()">
          <option value="">-- PILIH LAYANAN --</option>
          <option value="berkala">Service Berkala</option><option value="check rem 4 roda">Check Rem 4 Roda</option><option value="ganti oli">Ganti Oli Saja</option>
        </select>
      </div>
    </div>
  </div>

  <div class="no-print mb-4 row g-2">
    <div class="col-md-6">
      <div class="input-group input-group-sm">
        <span class="input-group-text bg-primary text-white fw-bold">🛠️ JASA</span>
        <input type="text" id="mJasaNama" class="form-control" placeholder="Nama Jasa/Pekerjaan">
        <input type="text" id="mJasaHarga" class="form-control w-25" placeholder="Harga" onkeyup="formatInputRupiah(this)">
        <button class="btn btn-primary" onclick="addManualJasa()"><i class="bi bi-plus-lg"></i></button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group input-group-sm">
        <span class="input-group-text bg-success text-white fw-bold">📦 PART</span>
        <input type="text" id="mPartNama" class="form-control" placeholder="Nama Part/Bahan">
        <input type="number" id="mPartQty" class="form-control" style="max-width:55px" value="1">
        <input type="text" id="mPartHarga" class="form-control w-25" placeholder="Harga" onkeyup="formatInputRupiah(this)">
        <button class="btn btn-success" onclick="addManualPart()"><i class="bi bi-plus-lg"></i></button>
      </div>
    </div>
  </div>

  <div class="table-responsive">
    <table class="table align-middle">
      <thead>
        <tr class="table-header text-center">
          <th width="40%" class="text-start ps-3 py-3">DESKRIPSI PEKERJAAN & PART</th>
          <th width="15%">BIAYA JASA</th>
          <th width="10%">QTY</th>
          <th width="15%">HARGA SATUAN</th>
          <th width="20%" class="text-end pe-3">SUBTOTAL</th>
        </tr>
      </thead>
      <tbody id="displayArea"></tbody>
    </table>
  </div>

  <div class="row mt-3 align-items-center">
    <div class="col-md-7">
       <div class="p-3 rounded bg-light small text-muted border-start border-4 border-primary">
         <strong>KETERANGAN:</strong><br>
         - Estimasi biaya bersifat sementara berdasarkan diagnosa awal.<br>
         - Berlaku selama 14 hari sejak tanggal diterbitkan.<br>
         - Harga sudah termasuk PPN.
       </div>
    </div>
    <div class="col-md-5">
      <div class="total-display">
        <small class="fw-bold">GRAND TOTAL ESTIMASI</small>
        <span class="total-amount">Rp <span id="grandTotal">0</span></span>
      </div>
    </div>
  </div>

  <div class="row mt-5">
    <div class="col-12 text-end">
      <p class="small mb-0">Makassar, <span id="currentDate"></span></p>
      <p class="fw-bold small mb-0">SERVICE ADVISOR,</p>
      <div class="signature-name">ISMAIL PRATAMA ILHAM</div>
    </div>
  </div>

  <div class="text-center mt-5 no-print d-flex justify-content-center gap-3">
    <button class="btn btn-outline-danger px-4 fw-bold" onclick="location.reload()">RESET FORM</button>
    <button class="btn btn-dark px-5 fw-bold" onclick="window.print()"><i class="bi bi-printer me-2"></i>SIMPAN PDF / CETAK</button>
  </div>
</div>

<script>
  let allData = []; 
  let manualJasaItems = [];
  let manualPartItems = [];

  const FIXED_JASA = { "berkala": 690000, "check rem 4 roda": 210000, "ganti oli": 45000 };

  window.onload = () => {
    document.getElementById('currentDate').innerText = new Date().toLocaleDateString('id-ID', {day: 'numeric', month: 'long', year: 'numeric'});
    try {
      google.script.run.withSuccessHandler(data => { allData = data; updateTable(); }).getHargaData();
    } catch(e) { updateTable(); }
  };

  function formatInputRupiah(el) {
    let val = el.value.replace(/[^0-9]/g, '');
    if (val) el.value = parseInt(val).toLocaleString('id-ID');
  }

  function addManualJasa() {
    const nama = document.getElementById('mJasaNama').value.trim();
    const harga = parseFloat(document.getElementById('mJasaHarga').value.replace(/\./g, '')) || 0;
    if (nama && harga > 0) {
      manualJasaItems.push({ nama, harga });
      document.getElementById('mJasaNama').value = '';
      document.getElementById('mJasaHarga').value = '';
      updateTable();
    }
  }

  function addManualPart() {
    const nama = document.getElementById('mPartNama').value.trim();
    const qty = parseFloat(document.getElementById('mPartQty').value) || 1;
    const harga = parseFloat(document.getElementById('mPartHarga').value.replace(/\./g, '')) || 0;
    if (nama && harga > 0) {
      manualPartItems.push({ nama, qty, harga });
      document.getElementById('mPartNama').value = '';
      document.getElementById('mPartHarga').value = '';
      document.getElementById('mPartQty').value = '1';
      updateTable();
    }
  }

  function updateTable() {
    const type = document.getElementById('typeSelect').value;
    const cat = document.getElementById('categorySelect').value;
    const area = document.getElementById('displayArea');
    let total = 0;
    area.innerHTML = '';

    // --- GRUP JASA ---
    area.innerHTML += `<tr><td colspan="5" class="category-divider ps-3">I. BIAYA JASA (ONGKOS KERJA)</td></tr>`;
    let hasJasa = false;
    
    if (FIXED_JASA[cat]) {
      total += FIXED_JASA[cat];
      area.innerHTML += renderRow("jasa", cat, FIXED_JASA[cat]);
      hasJasa = true;
    }
    manualJasaItems.forEach((item, idx) => {
      total += item.harga;
      area.innerHTML += renderRow("jasa", item.nama, item.harga, idx);
      hasJasa = true;
    });
    if(!hasJasa) area.innerHTML += '<tr><td colspan="5" class="text-center text-muted py-2 small italic">- Belum ada input jasa -</td></tr>';

    // --- GRUP PART ---
    area.innerHTML += `<tr><td colspan="5" class="category-divider ps-3">II. SUKU CADANG & BAHAN</td></tr>`;
    let hasPart = false;

    const dbParts = allData.filter(i => (type==="" || i['Tipe Mobil']?.includes(type)) && (cat==="" || i['Kategori']?.includes(cat)));
    dbParts.forEach(p => {
      let q = parseFloat(p['Qty']) || 1; let h = parseFloat(p['Harga Part']) || 0;
      total += (q*h);
      area.innerHTML += renderRow("part", p['Nama Part'], h, null, q);
      hasPart = true;
    });
    manualPartItems.forEach((p, idx) => {
      let sub = p.qty * p.harga; total += sub;
      area.innerHTML += renderRow("part", p.nama, p.harga, idx, p.qty);
      hasPart = true;
    });
    if(!hasPart) area.innerHTML += '<tr><td colspan="5" class="text-center text-muted py-2 small italic">- Belum ada input suku cadang -</td></tr>';

    document.getElementById('grandTotal').innerText = total.toLocaleString('id-ID');
  }

  function renderRow(mode, name, price, idx = null, qty = 1) {
    if (mode === "jasa") {
      return `<tr class="row-jasa">
        <td class="ps-3 fw-bold"><span class="badge-tag badge-jasa">Jasa</span>${name.toUpperCase()} 
        ${idx!==null ? `<i class="bi bi-x-circle text-danger no-print ms-1 pointer" onclick="manualJasaItems.splice(${idx},1);updateTable()"></i>` : ''}</td>
        <td class="text-end fw-bold text-primary">Rp ${price.toLocaleString('id-ID')}</td>
        <td class="text-center">-</td><td class="text-center">-</td>
        <td class="text-end pe-3 fw-bold">Rp ${price.toLocaleString('id-ID')}</td>
      </tr>`;
    } else {
      let sub = price * qty;
      return `<tr class="row-part">
        <td class="ps-3 fw-bold"><span class="badge-tag badge-part">Part</span>${name.toUpperCase()} 
        ${idx!==null ? `<i class="bi bi-x-circle text-danger no-print ms-1 pointer" onclick="manualPartItems.splice(${idx},1);updateTable()"></i>` : ''}</td>
        <td class="text-center">-</td><td class="text-center fw-bold">${qty}</td>
        <td class="text-end">Rp ${price.toLocaleString('id-ID')}</td>
        <td class="text-end pe-3 fw-bold">Rp ${sub.toLocaleString('id-ID')}</td>
      </tr>`;
    }
  }
</script>
</body>
</html>