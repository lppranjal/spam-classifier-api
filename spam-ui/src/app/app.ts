import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule, HttpClientModule, CommonModule],
  template: `
    <div class="container">
  <h1>Spam Classifier</h1>

  <textarea
    [(ngModel)]="message"
    placeholder="Type or paste text..."
    rows="6"
  ></textarea>

  <button (click)="classify()">Classify</button>

  <p *ngIf="result !== null">
    Result: <strong>{{ result }}</strong>
  </p>
</div>
  `,
  styles: [`
    body { font-family: sans-serif; background:#fafafa; }
.container { max-width:480px; margin:40px auto; padding:20px; background:#fff; border:1px solid #ddd; }
textarea { width:100%; font-size:1rem; }
button { margin-top:10px; padding:8px 16px; }

    `],
})
export class App {
  protected readonly title = signal('spam-ui');
  message = '';
  result: string | null = null;

  constructor(private http: HttpClient) {}

  classify() {
    if (!this.message.trim()) { return; }
    this.http
      .post<any>('https://spam-classifier-api-vrk2.onrender.com/predict', {
        text: this.message,
      })
      .subscribe(
        (resp) => (this.result = resp.result === 'spam' ? 'Spam' : 'Ham'),
        (err) => (this.result = 'Error')
      );
  }
}
