export enum ROLES {
  ROLE_USER = "ROLE_USER",
}

export default class User {
  private _id!: number;
  private _email!: string;
  private _roles!: ROLES[];
  private _firstName!: string;
  private _lastName!: string;
  private _sessionId?: string;

  constructor(datas: any) {
    this.id = datas.id;
    this.email = datas.email;
    this.roles = datas.roles;
    this.firstName = datas.firstName;
    this.lastName = datas.lastName;
    this.sessionId = datas.sessionId;
  }

  get id(): number {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }

  get email(): string {
    return this._email;
  }

  set email(value: string) {
    this._email = value;
  }

  get roles(): ROLES[] {
    return this._roles;
  }

  set roles(value: ROLES[]) {
    this._roles = value;
  }

  get firstName(): string {
    return this._firstName;
  }

  set firstName(value: string) {
    this._firstName = value;
  }

  get lastName(): string {
    return this._lastName;
  }

  set lastName(value: string) {
    this._lastName = value;
  }

  get sessionId(): string | undefined {
    return this._sessionId;
  }

  set sessionId(value: string | undefined) {
    this._sessionId = value;
  }

  get isUser(): boolean {
    return this._roles.includes(ROLES.ROLE_USER);
  }
}
