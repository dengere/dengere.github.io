---
layout: course
title: "Veri Yapıları ve Algoritmalar (Test 5)"
summary: "Temel veri yapıları, karmaşıklık analizi ve algoritmik problem çözme teknikleri."
categories:
  - "Temel Programlama ve Bilgisayar Bilimleri"
order: 5
duration: "100 saat"
instructors:
  - "Necati Ergin"

sessions:
  - start_date: 2026-09-05
    schedule:
      - "Cumartesi 10:00 - 13:00"
      - "Pazar 10:00 - 13:00"
    instructor: "Necati Ergin"
    format: "in_person"
    note: "Tamamlanan dönem"
---

## Kurs Hakkında

Bu eğitimde POSIX standartları ve Linux işletim sistemi mimarisi üzerinde doğrudan sistem çağrıları (system calls) kullanılarak düşük seviyeli uygulama geliştirme teknikleri ele alınır.

## Kurs İçeriği

### Dosya Sistemi ve G/Ç İşlemleri
* Düşük seviyeli dosya tanımlayıcıları (`open`, `read`, `write`, `lseek`)
* Dosya kilitleme mekanizmaları ve bellek eşlemeli dosyalar (`mmap`)

### Süreç ve İş Parçacığı Yönetimi
* Süreç oluşturma ve yaşam döngüsü (`fork`, `exec`, `wait`)
* POSIX Threads (`pthread`) ile eşzamanlılık ve senkronizasyon (`mutex`, `semaphore`, `condition variable`)

### Süreçler Arası İletişim (IPC) ve Ağ Programlama
* İsimsiz ve isimli borular (`pipe`, `FIFO`), paylaşılan bellek (`shared memory`) ve mesaj kuyrukları
* Soket programlama temelleri (TCP/UDP istemci-sunucu mimarisi)